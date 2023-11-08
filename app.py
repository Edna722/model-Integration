from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np  # Import numpy for reshaping data

app = Flask(__name__)

# Load the dataset
dataset_path = "C:/Users/wanji/Desktop/integration and development/Feature_Engineered_Dataset (1).csv"
data = pd.read_csv(dataset_path)

# Assuming the target column name is 'Total_Unemployment'
X = data.iloc[:, :-1]  # Features (all columns except the target)
y = data.iloc[:, -1]   # Target variable (the last column)

# Load the trained model
model_path = "C:/Users/wanji/Desktop/integration and development/best_random_forest_model.pkl"
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Welcome to the prediction service."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        predictions = []
        for item in request.json:
            prediction = model.predict(np.array(list(item.values())).reshape(1, -1))
            predictions.append({'Total_Unemployment': prediction[0]})
        
        return jsonify(predictions)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
