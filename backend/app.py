from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model/melhor_modelo.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de predição de câncer de mama online"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        features = [[
            float(data["radius_mean"]),
            float(data["texture_mean"]),
            float(data["perimeter_mean"]),
            float(data["area_mean"]),
            float(data["smoothness_mean"]),
            float(data["concavity_mean"]),
            float(data["concave_points_mean"]),
            float(data["symmetry_mean"]),
        ]]

        prediction = int(model.predict(features)[0])
        diagnosis = "Maligno" if prediction == 1 else "Benigno"

        return jsonify({
            "prediction": prediction,
            "diagnosis": diagnosis
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)