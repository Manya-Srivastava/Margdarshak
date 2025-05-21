from flask import Flask, request, jsonify
import psycopg2
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained delay prediction model
model = joblib.load('optimized_gradient_boosting_model.pkl')  # Update this path with your actual model file

# Database connection details
DB_CONFIG = {
    'host': 'localhost',  # Replace with your host
    'dbname': 'bus_route_optimization',  # Replace with your database name
    'user': 'bus',  # Replace with your PostgreSQL username
    'password': '1234'  # Replace with your PostgreSQL password
}

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

# API endpoint for delay prediction
@app.route('/predict_delay', methods=['POST'])
def predict_delay():
    """
    Predict bus delay based on input features.
    """
    try:
        # Parse input JSON from the user
        data = request.json
        required_features = ['normalized_travel_time', 'normalized_temperature', 
                             'traffic_impact', 'weather_impact']
        
        # Check if all required features are present
        for feature in required_features:
            if feature not in data:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
        
        # Prepare data for prediction
        input_features = pd.DataFrame([[
            data['normalized_travel_time'],
            data['normalized_temperature'],
            data['traffic_impact'],
            data['weather_impact']
        ]], columns=required_features)
        
        # Predict the delay using the model
        predicted_delay = model.predict(input_features)[0]
        
        # Return the prediction result
        return jsonify({'predicted_delay': round(predicted_delay, 2)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
