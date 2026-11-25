
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("student_model.pkl")


@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction=None,
        study_hours=None,
        attendance=None,
        previous_marks=None,
        error=None
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get student details
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])

        # Validate input
        if not 0 <= study_hours <= 24:
            raise ValueError("Study hours must be between 0 and 24.")

        if not 0 <= attendance <= 100:
            raise ValueError("Attendance must be between 0 and 100.")

        if not 0 <= previous_marks <= 100:
            raise ValueError("Previous marks must be between 0 and 100.")

        # Prepare input for the model
        input_data = pd.DataFrame(
            [[study_hours, attendance, previous_marks]],
            columns=[
                "study_hours",
                "attendance",
                "previous_marks"
            ]
        )

        # Predict final marks
        prediction = float(model.predict(input_data)[0])

        # Keep prediction within 0-100
        prediction = max(0, min(100, prediction))

        

        return render_template(
    "index.html",
    prediction=round(prediction, 2),
    study_hours=study_hours,
    attendance=attendance,
    previous_marks=previous_marks,
    error=None,
    show_results=True
)

    except ValueError as e:
        return render_template(
            "index.html",
            prediction=None,
            error=str(e)
        )

    except Exception as e:
        app.logger.exception("Prediction failed")
        return render_template(
            "index.html",
            prediction=None,
            error="Something went wrong. Please try again."
        )


if __name__ == "__main__":
    app.run(debug=True)
