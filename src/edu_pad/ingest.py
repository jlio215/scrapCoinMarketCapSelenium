import pandas as pd
from database import DataBase

def ingest_data(df: pd.DataFrame, table_name: str = "crypto_analisis"):
    db = DataBase()
    db.insert_data(df, table_name)
    print(f"✅ Inserción en BD completada (tabla: {table_name}).")

if __name__ == "__main__":
    try:
        ruta_in = "static/csv/criptomonedas_clean.csv"
        df_clean = pd.read_csv(ruta_in, sep=';', encoding='utf-8-sig')
        print(f"✅ Lectura de {ruta_in} exitosa. Shape:", df_clean.shape)

        ingest_data(df_clean)
    except Exception as e:
        print(f"❌ Error en ingest.py: {e}")
        raise
