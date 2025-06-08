from database import DataBase
import pandas as pd

def ingest_data(df: pd.DataFrame, table_name: str = "crypto_analisis"):
    try:
        db = DataBase()
        db.insert_data(df, table_name)
        print(f"✅ Datos insertados en la base de datos en la tabla '{table_name}'.")
    except Exception as e:
        print(f"❌ Error al insertar los datos en la base de datos: {e}")

if __name__ == "__main__":
    print("Este módulo requiere un DataFrame de entrada.")
