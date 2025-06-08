from dataweb import Dataweb
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        scraper = Dataweb()
        df_clean = scraper.limpieza_datos(df)
        print("✅ Limpieza de datos completada.")
        return df_clean
    except Exception as e:
        print(f"❌ Error en la limpieza de datos: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Modo prueba: solo para verificar que corre
    print("Este módulo requiere un DataFrame de entrada.")
