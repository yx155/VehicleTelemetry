
function showVehicleDetails(vehicleid) {
    fetch('data/vehicles.json')
        .then(response => response.json())
        .then(data => {
            const vehicle = data.find(v => v.vehicleid == vehicleid);
            if (vehicle) {
                const alertIcon = vehicle.alert === 0 
                    ? 'images/success.png' 
                    : vehicle.alert === -1 
                        ? 'images/warning.png' 
                        : 'images/caution.png';
                
                const vehicleDetailsContent = `
                    <div class="header-container">
                        <img src="${alertIcon}" alt="Alert Icon" class="alert-icon">
                        <h1>${vehicle.maintenance == "" ? "No Maintenance Due" : vehicle.maintenance + " due " + vehicle.due}</h1>
                    </div>
                    <p><strong>Vehicle ID:</strong> ${vehicle.vehicleid}</p>
                    <p><strong>Make:</strong> ${vehicle.make}</p>
                    <p><strong>Model:</strong> ${vehicle.model}</p>
                    <p><strong>Powertrain:</strong> ${vehicle.type}</p>
                    <p><strong>Mileage:</strong> ${vehicle.mileage}</p>
                    <p><strong>Time in FedEx Service:</strong> ${vehicle.age} years</p>
                    <p><strong>Average Engine Idle Time:</strong> ${vehicle.idle} minutes</p>
                    <p><strong>Last Maintenance:</strong> ${vehicle.lastMaintenance}</p>
                    <p><strong>Date Last Maintenance:</strong> ${vehicle.dateLastMaintenance}</p>
                `;
                document.getElementById('vehicle-details').innerHTML = vehicleDetailsContent;
            } else {
                document.getElementById('vehicle-details').innerHTML = `
                    <h1>Vehicle not found</h1>
                `;
            }
        })
        .catch(error => console.error('Error loading vehicle data:', error));
    
    const myModal = new bootstrap.Modal(document.getElementById('vehicleDetailsModal'));
    myModal.show();
}
