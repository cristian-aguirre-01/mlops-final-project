import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train(train_dataset_file: str, model_path: str) -> None:
    """Entrena el modelo usando un pipeline que encapsula todo el preprocesamiento."""
    df = pd.read_csv(train_dataset_file, sep=";")

    X = df.drop('Attrition', axis=1)
    y = df['Attrition']

    # Separar columnas por tipo
    categorical_cols = [
        'BusinessTravel', 'Department', 'EducationField',
        'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime'
    ]
    # Filtrar solo las que existen en el dataframe (por si data_prep eliminó alguna constante)
    categorical_cols = [col for col in categorical_cols if col in X.columns]
    numerical_cols = [col for col in X.columns if col not in categorical_cols]

    print(f"Categóricas: {categorical_cols}")
    print(f"Numéricas: {numerical_cols}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), categorical_cols)
    ])

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('lr_clf', LogisticRegression(solver='liblinear', penalty='l1'))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)

    print(f"Pipeline guardado en: {model_path}")


if __name__ == '__main__':
    # Path del dataset de entrenamiento
    train_path = "data/training/train_dataset.csv"
    # PATH del modelo a guardar
    model_path = "models/model_lr.pkl"
    train(train_path, model_path)
