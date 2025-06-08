import pandas as pd
import sqlite3
from database import DataBase

def ingest_data(df: pd.DataFrame, table_name: str = "crypto_analisis"):
    db = DataBase()
    # 1. Insertar datos
    db.insert_data(df, table_name)
    print(f"✅ Inserción en BD completada (tabla: {table_name}).")

    # 2. Verificar con consulta SQL directa
    try:
        conn = sqlite3.connect(db.db_name)
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} LIMIT 10;"
        print(f"🔍 Ejecutando consulta: {query}")
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]
        print("✅ Primeras 10 filas desde la base de datos:")
        # Imprimir cabeceras
        print(" | ".join(col_names))
        # Imprimir filas
        for row in rows:
            print(" | ".join(str(item) for item in row))
        conn.close()
    except Exception as err:
        print(f"❌ Error al consultar la base de datos: {err}")

if __name__ == "__main__":
    try:
        ruta_in = "static/csv/criptomonedas_clean.csv"
        df_clean = pd.read_csv(ruta_in, sep=';', encoding='utf-8-sig')
        print(f"✅ Lectura de {ruta_in} exitosa. Shape:", df_clean.shape)

        ingest_data(df_clean)
    except Exception as e:
        print(f"❌ Error en ingest.py: {e}")
        raise
