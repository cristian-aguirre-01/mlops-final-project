import pandas as pd

def data_preparation(raw_dataset_file: str, train_dataset_file: str) -> None:
    """Limpia el dataset raw y guarda el dataset de entrenamiento SIN transformaciones de encoding."""
    df = pd.read_csv(raw_dataset_file)

    # Remover filas duplicadas
    df.drop_duplicates(inplace=True)

    # Remover columnas constantes (un solo valor único) que no aportan información
    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    if constant_cols:
        print(f"Columnas constantes eliminadas: {constant_cols}")
        df.drop(columns=constant_cols, inplace=True)

    print(f"Shape final: {df.shape}")
    print(df.head())

    df.to_csv(train_dataset_file, index=False, sep=";")
    print(f"Dataset guardado en: {train_dataset_file}")


if __name__=='__main__':
    # Path de archivo raw
    origin_path = "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    # Path donde se guardara el dataset entrenado
    training_path = "data/training/train_dataset.csv"

    data_preparation(origin_path, training_path)


