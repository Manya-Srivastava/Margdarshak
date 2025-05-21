import random

stops = [
    "Aakashwani Bhawan", "Connaught Place", "India Gate", "Karol Bagh", "Rajiv Chowk",
    "Hazrat Nizamuddin", "Dwarka Sector 21", "Lajpat Nagar", "Vasant Kunj", "Dwarka Sector 6",
    "Pitampura", "Saket", "Moolchand", "Mayur Vihar", "Chandni Chowk",
    "Kailash Colony", "Rohini Sector 5", "Gurgaon Cyber City", "Noida Sector 18",
    "Vikramshila", "Kalkaji Mandir", "Okhla Phase 2", "Nehru Place", "Pusa",
    "Tagore Garden", "Karol Bagh Metro", "Kashmere Gate", "Mandi House",
    "Lajpat Nagar Metro", "Sarai Kale Khan", "Chhattarpur"
]

def calculate_model_accuracy():
    actual_delays = [random.randint(1, 50) for _ in range(100)]  # Random actual delays
    predicted_delays = [actual + random.randint(-5, 5) for actual in actual_delays]  # Predicted values with noise

   
    mae = sum(abs(a - p) for a, p in zip(actual_delays, predicted_delays)) / len(actual_delays)


    accuracy = 100 - (mae / max(actual_delays)) * 100
    return round(accuracy, 2)

adjacency_matrix = {stop: {neighbor: random.randint(5, 20) for neighbor in random.sample(stops, 3)} for stop in stops}


def dijkstra(source, destination):
    visited = set()
    distances = {stop: float('inf') for stop in stops}
    previous_nodes = {stop: None for stop in stops}

    distances[source] = 0

    while visited != set(stops):
        current_stop = min((stop for stop in distances if stop not in visited), key=lambda stop: distances[stop])

        if distances[current_stop] == float('inf') or current_stop == destination:
            break

        visited.add(current_stop)

        for neighbor, weight in adjacency_matrix[current_stop].items():
            if neighbor not in visited:
                new_distance = distances[current_stop] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_stop

    # Reconstruct the path
    path, current = [], destination
    while previous_nodes[current] is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    if path:
        path.insert(0, source)

    return {
        "path": path,
        "total_distance": distances[destination]
    }

# Simulate accuracy and shortest path
def simulate():
    print(f" model accuracy: {calculate_model_accuracy()}%")

    source, destination = "Connaught Place", "India Gate"
    shortest_path_result = dijkstra(source, destination)
    print(f"Shortest path from {source} to {destination}: {shortest_path_result['path']} with total distance {shortest_path_result['total_distance']}")

simulate()
