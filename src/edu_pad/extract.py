from dataweb import Dataweb
import pandas as pd
import os

def extract_data() -> pd.DataFrame:
    from dataweb import Dataweb
    scraper = Dataweb()
    df = scraper.obtener_datos()
    print("✅ Extracción de datos completada.")
    return df

if __name__ == "__main__":
    df = extract_data()
    os.makedirs("static/csv", exist_ok=True)
    df.to_csv("static/csv/criptomonedas.csv", index=False, sep=';', encoding='utf-8-sig')
    print("✅ Guardado CSV en static/csv/criptomonedas.csv")
