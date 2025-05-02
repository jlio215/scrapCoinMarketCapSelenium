
from dataweb import Dataweb
import pandas as pd



def main():
    dataweb = Dataweb()
    df = pd.DataFrame(dataweb.obtener_datos())
    df.to_csv("data_web.csv", index=False)



# Uso de la clase
if __name__ == "__main__":
    scraper = Dataweb()
    datos = scraper.obtener_datos()
    main()
    
    if not datos.empty:
        print("Datos obtenidos exitosamente:")
        print(datos.head())
    else:
        print("No se pudieron obtener los datos.")