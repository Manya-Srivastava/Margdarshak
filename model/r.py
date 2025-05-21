import random
import time

# Simulated data for stops, routes, and buses
stops = [
    "Aakashwani Bhawan", "Connaught Place", "India Gate", "Karol Bagh", "Rajiv Chowk", "Hazrat Nizamuddin",
    "Dwarka Sector 21", "Lajpat Nagar", "Vasant Kunj", "Dwarka Sector 6", "Pitampura", "Saket", "Moolchand",
    "Mayur Vihar", "Chandni Chowk", "Kailash Colony", "Rohini Sector 5", "Gurgaon Cyber City", "Noida Sector 18",
    "Vikramshila", "Kalkaji Mandir", "Okhla Phase 2", "Nehru Place", "Pusa", "Tagore Garden", "Karol Bagh Metro",
    "Kashmere Gate", "Mandi House", "Lajpat Nagar Metro", "Sarai Kale Khan", "Chhattarpur"
]

# Bus data simulation
buses = [
    {
        "bus_id": f"Bus-{i}",
        "current_stop": random.choice(stops),
        "traffic_level": random.choice(["Low", "Moderate", "High"]),
        "base_time": random.randint(10, 30)
    }
    for i in range(1, 51)
]

def generate_traffic_delay(traffic_level):
    if traffic_level == "Low":
        return random.randint(1, 5)
    elif traffic_level == "Moderate":
        return random.randint(5, 15)
    elif traffic_level == "High":
        return random.randint(15, 35)

def calculate_route_time(start, destination):
    base_time = random.randint(10, 30)
    traffic_level = random.choice(["Low", "Moderate", "High"])
    delay = generate_traffic_delay(traffic_level)
    total_time = base_time + delay
    return {
        "start": start,
        "destination": destination,
        "base_time": base_time,
        "traffic_level": traffic_level,
        "delay": delay,
        "total_time": total_time
    }

def simulate_user_request(user_location, destination):
    # Fetch nearby buses
    nearby_buses = [
        {
            "bus_id": bus["bus_id"],
            "current_stop": bus["current_stop"],
            "eta": random.randint(1, 15)
        }
        for bus in buses if bus["current_stop"] == user_location
    ]

    # Calculate routes
    routes = []
    for _ in range(3):  # Generate 3 route options
        route_info = calculate_route_time(user_location, destination)
        routes.append(route_info)

    # Sort routes by total time
    routes.sort(key=lambda x: x["total_time"])

    # Best route
    best_route = routes[0]

    return {
        "user_location": user_location,
        "destination": destination,
        "best_route": best_route,
        "nearby_buses": nearby_buses
    }

# Example user request
user_location = "Connaught Place"
destination = "India Gate"
result = simulate_user_request(user_location, destination)

# Output simulated data
print("User Location:", result["user_location"])
print("Destination:", result["destination"])
print("Best Route:")
print("  Start:", result["best_route"]["start"])
print("  Destination:", result["best_route"]["destination"])
print("  Base Time (mins):", result["best_route"]["base_time"])
print("  Traffic Level:", result["best_route"]["traffic_level"])
print("  Delay (mins):", result["best_route"]["delay"])
print("  Total Time (mins):", result["best_route"]["total_time"])
print("Nearby Buses:")
for bus in result["nearby_buses"]:
    print(f"  Bus ID: {bus['bus_id']}, Current Stop: {bus['current_stop']}, ETA: {bus['eta']} mins")
