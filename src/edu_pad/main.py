from dataweb import Dataweb

scraper = Dataweb()
df = scraper.obtener_datos()

if not df.empty:
    df_limpio = scraper.limpieza_datos(df)
    df_limpio.to_csv(
    'criptomonedas.csv',
    index=False,
    sep=';',
    encoding='utf-8-sig'
)
    print("✅ Datos limpios guardados en criptomonedas.csv")
    print(df_limpio.head())
else:
    print("❌ No se pudo obtener la información.")
