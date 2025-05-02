import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Nuevo: Configurar opciones de Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

class Dataweb:
    def __init__(self):
        self.url = "https://coinmarketcap.com/"
        
        # Configurar Chrome en modo headless (sin interfaz gráfica)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecutar sin abrir ventana
        chrome_options.add_argument("--disable-gpu")  # Mejorar rendimiento
        chrome_options.add_argument("--window-size=1920x1080")  # Tamaño de ventana virtual
        
        # Inicializar el driver con las opciones
        self.driver = webdriver.Chrome(options=chrome_options)  # Usar 'options' en lugar de 'chrome_options' en versiones recientes
    
    def obtener_datos(self):
        try:
            self.driver.get(self.url)
            
            # Aceptar cookies si es necesario
            try:
                accept_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept') or contains(., 'Aceptar')]"))
                )
                accept_button.click()
            except:
                pass
            
            all_data = []
            
            for _ in range(8):  # 10 iteraciones para obtener ~100 criptomonedas
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
                
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                
                # Extraer títulos de columnas
                thead = soup.find('thead')
                column_titles = []
                if thead:
                    th_elements = thead.find_all('th')
                    for th in th_elements:
                        title = th.get_text(strip=True)
                        if title:
                            column_titles.append(title)
                        else:
                            p = th.find('p')
                            if p:
                                column_titles.append(p.get_text(strip=True))
                            else:
                                column_titles.append("")
                
                # Extraer datos de las filas
                table = soup.find('table')
                rows = []
                if table:
                    tbody = table.find('tbody')
                    if tbody:
                        for tr in tbody.find_all('tr')[:10]:  # Solo 10 filas por iteración
                            row = [td.get_text(strip=True) for td in tr.find_all('td')]
                            rows.append(row)
                
                all_data.extend(rows)
                
                # Scroll hacia abajo y esperar
                self.driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(3)  # Esperar 5 segundos para carga dinámica
            
            self.driver.quit()  # Cerrar navegador al finalizar
            
            # Crear DataFrame (solo las primeras 100 filas)
            df = pd.DataFrame(all_data[:100], columns=column_titles[:len(all_data[0])]) if all_data else pd.DataFrame()
            return df
        
        except Exception as err:
            print(f"Error en la función obtener_datos: {err}")
            self.driver.quit()
            return pd.DataFrame()