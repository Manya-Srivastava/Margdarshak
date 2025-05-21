import random
def generate_expected_data(user_location, destination, num_samples=10):
    expected_data = []
    for _ in range(num_samples):
        expected_time = random.randint(15, 35)  
        expected_data.append({
            "user_location": user_location,
            "destination": destination,
            "expected_time": expected_time
        })
    return expected_data

# Simulated predictions
def generate_predicted_data(expected_data):
    predicted_data = []
    for data in expected_data:
        # Add random noise to simulate predictions
        predicted_time = data["expected_time"] + random.randint(-5, 5)
        predicted_data.append({
            "user_location": data["user_location"],
            "destination": data["destination"],
            "predicted_time": predicted_time,
            "expected_time": data["expected_time"]
        })
    return predicted_data

# Calculate evaluation metrics
def evaluate_model(predicted_data):
    total_absolute_error = 0
    correct_predictions = 0
    total_samples = len(predicted_data)

    for data in predicted_data:
        error = abs(data["predicted_time"] - data["expected_time"])
        total_absolute_error += error
        if error <= 3:
            correct_predictions += 1

    # Calculate metrics
    mean_absolute_error = total_absolute_error / total_samples
    accuracy = (correct_predictions / total_samples) * 100

    return {
        "mean_absolute_error": mean_absolute_error,
        "accuracy": accuracy

user_location = "Connaught Place"
destination = "India Gate"

# Generate expected and predicted data
expected_data = generate_expected_data(user_location, destination)
predicted_data = generate_predicted_data(expected_data)

# Evaluate model
evaluation_results = evaluate_model(predicted_data)

# Print results
print("Evaluation Results:")
print("Mean Absolute Error (mins):", evaluation_results["mean_absolute_error"])
print("Accuracy (%):", evaluation_results["accuracy"])

print("\nPredictions vs. Expected:")
for data in predicted_data:
    print(f"User Location: {data['user_location']}, Destination: {data['destination']}, "
          f"Expected Time: {data['expected_time']} mins, Predicted Time: {data['predicted_time']} mins")
