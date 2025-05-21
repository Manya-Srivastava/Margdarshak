import random

# List of predefined stops and routes
stops = [
    "Aakashwani Bhawan", "Connaught Place", "India Gate", "Karol Bagh", "Rajiv Chowk",
    "Hazrat Nizamuddin", "Dwarka Sector 21", "Lajpat Nagar", "Vasant Kunj", "Dwarka Sector 6",
    "Pitampura", "Saket", "Moolchand", "Mayur Vihar", "Chandni Chowk",
    "Kailash Colony", "Rohini Sector 5", "Gurgaon Cyber City", "Noida Sector 18",
    "Vikramshila", "Kalkaji Mandir", "Okhla Phase 2", "Nehru Place", "Pusa",
    "Tagore Garden", "Karol Bagh Metro", "Kashmere Gate", "Mandi House",
    "Lajpat Nagar Metro", "Sarai Kale Khan", "Chhattarpur"
]

# Simulated traffic levels
traffic_levels = ["Low", "Moderate", "High"]

# Function to generate random delays based on traffic levels
def generate_delay(traffic_level):
    if traffic_level == "Low":
        return random.randint(1, 5)  
    elif traffic_level == "Moderate":
        return random.randint(5, 15)  
    elif traffic_level == "High":
        return random.randint(15, 35)  

# Function to simulate route optimization
def optimize_route(user_location, destination):
    random_traffic_level = random.choice(traffic_levels)
    delay = generate_delay(random_traffic_level)
    alternative_routes = [
        {
            "route": f"Fastest route via main roads to {destination}",
            "estimated_time": random.randint(10, 40)  # 10-40 minutes
        },
        {
            "route": f"Scenic route avoiding traffic to {destination}",
            "estimated_time": random.randint(20, 70)  # 20-70 minutes
        }
    ]

    # Randomly select an optimized route
    optimized_route = random.choice(alternative_routes)

    return {
        "user_location": user_location,
        "destination": destination,
        "traffic_level": random_traffic_level,
        "delay": delay,
        "optimized_route": optimized_route
    }
def get_nearby_buses(user_location):
    buses = [
        {"bus_id": "DL-101", "current_stop": "Connaught Place", "next_stop": "India Gate", "eta": random.randint(5, 15)},
        {"bus_id": "DL-102", "current_stop": "Karol Bagh", "next_stop": "Rajiv Chowk", "eta": random.randint(3, 13)},
        {"bus_id": "DL-103", "current_stop": "Lajpat Nagar", "next_stop": "Moolchand", "eta": random.randint(7, 17)},
        {"bus_id": "DL-104", "current_stop": "Hazrat Nizamuddin", "next_stop": "Dwarka Sector 21", "eta": random.randint(2, 12)},
    ]

    return [bus for bus in buses if bus["current_stop"] == user_location]

# Simulate user request
def simulate_user_request(user_location, destination):
    print(f"Simulating request for {user_location} to {destination}...")

    route_info = optimize_route(user_location, destination)
    nearby_buses = get_nearby_buses(user_location)

    print("Optimization Results:", route_info)
    print("Nearby Buses:", nearby_buses)

    return {"route_info": route_info, "nearby_buses": nearby_buses}

# Example: Simulate for a user at Connaught Place heading to India Gate
simulation_result = simulate_user_request("Connaught Place", "India Gate")
print(simulation_result)
