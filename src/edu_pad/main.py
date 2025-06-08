from extract import extract_data
from clean import clean_data
from ingest import ingest_data
import pandas as pd

def main():
    try:
        df = extract_data()

        if df.empty:
            print("❌ No se pudo obtener la información.")
            return

        df_clean = clean_data(df)
        
        if df_clean.empty:
            print("❌ La limpieza de datos falló o produjo un DataFrame vacío.")
            return

        df_clean.to_csv(
            'criptomonedas.csv',
            index=False,
            sep=';',
            encoding='utf-8-sig'
        )
        print("✅ Datos limpios guardados en criptomonedas.csv")

        ingest_data(df_clean)
        print("✅ Flujo de extracción, limpieza e ingestión finalizado correctamente.")
    except Exception as e:
        print(f"❌ Error general en el flujo principal: {e}")

if __name__ == "__main__":
    main()
