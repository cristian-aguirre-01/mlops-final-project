from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask("Mi Model ML App")
model = pickle.load(open("models/model_lr.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    input_features = request.get_json(force=True)
    print("INPUT:", input_features)

    # Crear DataFrame directamente, sin get_dummies
    df = pd.DataFrame([input_features])
    print(df.head())

    # El pipeline ya sabe cómo transformar (OneHotEncoder entrenado)
    prediction = model.predict(df)[0]
    print("PREDICTION:", prediction)
    if prediction == 'Yes':
        prediction = 1
    else:
        prediction = 0
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
