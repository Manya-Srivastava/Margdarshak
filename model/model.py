import random
import time

# Define some sample stops and traffic levels
stops = [
    "Aakashwani Bhawan", "Connaught Place", "India Gate", "Karol Bagh", "Rajiv Chowk",
    "Hazrat Nizamuddin", "Dwarka Sector 21", "Lajpat Nagar", "Vasant Kunj", "Dwarka Sector 6",
    "Pitampura", "Saket", "Moolchand", "Mayur Vihar", "Chandni Chowk",
    "Kailash Colony", "Rohini Sector 5", "Gurgaon Cyber City", "Noida Sector 18",
    "Vikramshila", "Kalkaji Mandir", "Okhla Phase 2", "Nehru Place", "Pusa",
    "Tagore Garden", "Karol Bagh Metro", "Kashmere Gate", "Mandi House",
    "Lajpat Nagar Metro", "Sarai Kale Khan", "Chhattarpur"
]

traffic_levels = ["Low", "Moderate", "High"]

def generate_traffic_delay(traffic_level):
    if traffic_level == "Low":
        return random.randint(1, 5)  # 1-5 minutes delay
    elif traffic_level == "Moderate":
        return random.randint(5, 15)  # 5-15 minutes delay
    else:  # High traffic
        return random.randint(15, 35)  # 15-35 minutes delay

# Generate route times
def calculate_route_time(start, destination):
    base_time = random.randint(10, 30)  # Base time in minutes
    random_traffic_level = random.choice(traffic_levels)
    traffic_delay = generate_traffic_delay(random_traffic_level)
    total_time = base_time + traffic_delay
    return total_time, random_traffic_level

# Simulate real-time optimization
def simulate_real_time_route(user_location, destination):
    print(f"Calculating best route from {user_location} to {destination}...")
    time.sleep(1)  # Simulating processing delay

    # Simulate available routes
    routes = [
        {
            "route_description": f"Fast route via main roads to {destination}",
            "route_time": calculate_route_time(user_location, destination)
        },
        {
            "route_description": f"Scenic route avoiding main traffic zones to {destination}",
            "route_time": calculate_route_time(user_location, destination)
        },
        {
            "route_description": f"Alternative back-road route to {destination}",
            "route_time": calculate_route_time(user_location, destination)
        }
    ]

    # Sort routes by estimated time
    routes.sort(key=lambda x: x["route_time"][0])

    best_route = routes[0]
    print(f"Best route selected: {best_route['route_description']} (ETA: {best_route['route_time'][0]} minutes)")

    # Return the best route
    return {
        "user_location": user_location,
        "destination": destination,
        "best_route": best_route["route_description"],
        "eta": best_route["route_time"][0],
        "traffic_level": best_route["route_time"][1]
    }

# Simulate nearby bus information
def get_nearby_buses(user_location):
    buses = [
        {"bus_id": "DL-201", "current_stop": "Connaught Place", "next_stop": "India Gate", "eta": random.randint(5, 15)},
        {"bus_id": "DL-202", "current_stop": "Karol Bagh", "next_stop": "Rajiv Chowk", "eta": random.randint(3, 13)},
        {"bus_id": "DL-203", "current_stop": "Lajpat Nagar", "next_stop": "Moolchand", "eta": random.randint(7, 17)},
        {"bus_id": "DL-204", "current_stop": "Hazrat Nizamuddin", "next_stop": "Dwarka Sector 21", "eta": random.randint(2, 12)},
    ]

    # Filter buses stopping near the user location
    nearby_buses = [bus for bus in buses if bus["current_stop"] == user_location]
    print(f"Nearby buses for {user_location}: {nearby_buses}")
    return nearby_buses

# Combine simulation of route and bus data
def simulate_user_request(user_location, destination):
    print(f"Simulating user request from {user_location} to {destination}...\n")
    route_info = simulate_real_time_route(user_location, destination)
    nearby_buses = get_nearby_buses(user_location)

    simulation_result = {
        "route_info": route_info,
        "nearby_buses": nearby_buses
    }
    return simulation_result

# Run a simulation example
if __name__ == "__main__":
    user_location = "Connaught Place"
    destination = "India Gate"
    result = simulate_user_request(user_location, destination)

    print("\nSimulation Results:")
    print(f"Route Information: {result['route_info']}")
    print(f"Nearby Buses: {result['nearby_buses']}")
