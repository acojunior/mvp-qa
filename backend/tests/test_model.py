import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def test_model_accuracy():
    # caminho do dataset
    url = "https://raw.githubusercontent.com/acojunior/mvp-software-inteligentes/refs/heads/main/breast-cancer.csv"
    df = pd.read_csv(url)

    # converter target
    df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

    # mesmas features usadas no notebook
    selected_features = [
        "radius_mean",
        "texture_mean",
        "perimeter_mean",
        "area_mean",
        "smoothness_mean",
        "concavity_mean",
        "concave points_mean",
        "symmetry_mean"
    ]

    X = df[selected_features]
    y = df["diagnosis"]

    # mesmo holdout usado no notebook
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=7,
        stratify=y
    )

    # caminho do modelo exportado
    model_path = os.path.join("model", "melhor_modelo.pkl")
    model = joblib.load(model_path)

    # predição
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # threshold mínimo aceitável
    assert accuracy >= 0.88, f"Acurácia abaixo do esperado: {accuracy:.4f}"