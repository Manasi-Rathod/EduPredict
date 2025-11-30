from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("placement_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            # Fetch and convert form data
            data = [
                float(request.form['prev_result']),
                float(request.form['cgpa']),
                float(request.form['academic']),
                float(request.form['internship']),
                float(request.form['extra_curricular']),
                float(request.form['communication']),
                float(request.form['projects'])
            ]

            # Scale and predict
            scaled_data = scaler.transform([data])
            pred = model.predict(scaled_data)[0]
            prediction = "Placed ✅" if pred == 1 else "Not Placed ❌"

        except ValueError:
            error = "Please enter valid numeric values in all fields."
        except Exception as e:
            error = f"An unexpected error occurred: {str(e)}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
