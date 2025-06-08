import pandas as pd
import os
from dataweb import Dataweb

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # tu método de limpieza original
    scraper = Dataweb()
    return scraper.limpieza_datos(df)

if __name__ == "__main__":
    try:
        ruta_in = "static/csv/criptomonedas.csv"
        ruta_out = "static/csv/criptomonedas_clean.csv"

        df = pd.read_csv(ruta_in, sep=';', encoding='utf-8-sig')
        print(f"✅ Lectura de {ruta_in} exitosa. Shape:", df.shape)

        df_clean = clean_data(df)
        print("✅ Limpieza de datos completada. Shape:", df_clean.shape)

        df_clean.to_csv(ruta_out, index=False, sep=';', encoding='utf-8-sig')
        print(f"✅ Guardado CSV limpio en {ruta_out}")
    except Exception as e:
        print(f"❌ Error en clean.py: {e}")
        raise
