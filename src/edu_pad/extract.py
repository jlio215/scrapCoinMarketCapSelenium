from dataweb import Dataweb
import pandas as pd

def extract_data() -> pd.DataFrame:
    try:
        scraper = Dataweb()
        df = scraper.obtener_datos()
        print("✅ Extracción de datos completada.")
        return df
    except Exception as e:
        print(f"❌ Error en la extracción de datos: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    extract_data()
