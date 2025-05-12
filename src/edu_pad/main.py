from dataweb import Dataweb
from database import DataBase

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
    database = DataBase()
    nombre_tabla = "crypto_analisis"
    database.insert_data(df_limpio,nombre_tabla)
    print("*************** Insertar los datos obtenidos en la base datos tabla: {}*********".format(nombre_tabla))
    print(df.shape)
    print(df.head())
    df_2 = database.read_data(nombre_tabla)
    print(df_2.shape)
    print(df_2.head())
    print("✅ Datos limpios guardados en criptomonedas.csv")
    print(df_limpio.head())
else:
    print("❌ No se pudo obtener la información.")