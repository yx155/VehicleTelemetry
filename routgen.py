import json
from datetime import datetime, timedelta
import random

# Generate sample data
couriers = [
    {"id": 101, "name": "John Smith", "route_number": "R1"},
    {"id": 102, "name": "Emily Davis", "route_number": "R2"},
    {"id": 103, "name": "Michael Brown", "route_number": "R3"},
    {"id": 104, "name": "Sarah Wilson", "route_number": "R4"},
    {"id": 105, "name": "David Johnson", "route_number": "R5"}
]

route_data = []

# Generate data for 100 route entries
for _ in range(100):
    courier = random.choice(couriers)
    date = (datetime.today() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
    
    stops = random.randint(3, 15)  # Number of stops
    elapsed_times = [random.randint(1, 15) for _ in range(stops)]  # Elapsed times at each stop
    distances = [round(random.uniform(0.5, 5.0), 2) for _ in range(stops - 1)]  # Distances between stops
    total_distance = round(sum(distances), 2)
    stop_times = [random.randint(1, 30) for _ in range(stops)]  # Stop times with engine off
    total_stop_time = sum(stop_times)
    engine_idle_time = total_stop_time - random.randint(5, 20)  # Simulated idle time

    # Departure and return time
    departure_time = datetime.strptime(f"{date} 07:00", '%Y-%m-%d %H:%M')
    return_time = departure_time + timedelta(hours=random.uniform(3, 8))
    
    # Create entry
    entry = {
        "courier": {
            "id": courier["id"],
            "name": courier["name"],
            "route_number": courier["route_number"]
        },
        "date": date,
        "departure_time": departure_time.strftime('%Y-%m-%d %H:%M'),
        "return_time": return_time.strftime('%Y-%m-%d %H:%M'),
        "stops": [
            {
                "stop_number": i + 1,
                "elapsed_time": elapsed_times[i],
                "distance_traveled": distances[i] if i < len(distances) else 0,
                "stop_time": stop_times[i]
            } for i in range(stops)
        ],
        "summary": {
            "total_miles_traveled": total_distance,
            "average_stop_time": round(total_stop_time / stops, 2),
            "total_stop_time": total_stop_time,
            "total_engine_idle_time": engine_idle_time
        }
    }

    route_data.append(entry)

# Convert to JSON format
routes_json = json.dumps(route_data, indent=4)

# Write the generated JSON data to a file named routes.json
output_file_path = 'c://PHD//ntwk//HI///routes.json'
with open(output_file_path, 'w') as file:
    file.write(routes_json)

print(f"JSON file created at {output_file_path}")
