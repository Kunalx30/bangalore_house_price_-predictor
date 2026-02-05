from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load cleaned dataset (for locations)
data = pd.read_csv("Cleaned_data.csv")
locations = sorted(data['location'].unique())

# Load trained Ridge model
with open("RidgeModel.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return render_template(
        'index.html',
        locations=locations
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form['location']
        bhk = float(request.form['bhk'])
        bath = float(request.form['bath'])
        sqft = float(request.form['sqft'])

        # Create input dataframe (VERY IMPORTANT: column names must match training)
        input_df = pd.DataFrame([{
            'location': location,
            'total_sqft': sqft,
            'bath': bath,
            'bhk': bhk
        }])

        prediction = model.predict(input_df)[0]
        price = round(prediction, 2)

        return render_template(
            'index.html',
            locations=locations,
            prediction_text=f"Estimated Price: ₹ {price} Lakhs"
        )

    except Exception as e:
        return render_template(
            'index.html',
            locations=locations,
            prediction_text="Error in prediction. Please check input values."
        )


if __name__ == "__main__":
    app.run(debug=True, port=5001)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
