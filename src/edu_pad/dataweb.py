import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dataweb:
    def __init__(self):
        self.url = "https://coinmarketcap.com/"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')                   # necesario en contenedores
        options.add_argument('--disable-dev-shm-usage')        # usa /tmp en lugar de /dev/shm
        options.add_argument('--user-data-dir=/tmp/chrome-data')  # perfil limpio en cada run
        
        self.driver = webdriver.Chrome(options=options)
        self.column_titles = None

    def obtener_datos(self):
        try:
            self.driver.get(self.url)
            # Aceptar cookies
            try:
                btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(., 'Accept') or contains(., 'Aceptar')]")
                    )
                )
                btn.click()
            except:
                pass

            all_rows = []
            # Extraemos bloques de 10 filas hasta completar ~100
            while len(all_rows) < 100:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')

                # Capturar títulos una sola vez y descartar el '#'
                if self.column_titles is None:
                    thead = soup.find('thead')
                    titles = []
                    if thead:
                        for th in thead.find_all('th'):
                            txt = th.get_text(strip=True) or ""
                            if not txt:
                                p = th.find('p')
                                txt = p.get_text(strip=True) if p else ""
                            titles.append(txt)
                    self.column_titles = titles[1:]

                tbody = soup.find('tbody')
                if not tbody:
                    break

                trs = tbody.find_all('tr')
                start = len(all_rows)
                block = trs[start:start + 10]
                if not block:
                    break

                for tr in block:
                    cols = [td.get_text(strip=True) for td in tr.find_all('td')]
                    all_rows.append(cols[1:])  # descartar ranking

                # Scroll y espera 2s
                self.driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(2)

            self.driver.quit()

            if not all_rows or not self.column_titles:
                return pd.DataFrame()

            return pd.DataFrame(all_rows[:100], columns=self.column_titles)

        except Exception as err:
            print(f"Error en obtener_datos: {err}")
            try:
                self.driver.quit()
            except:
                pass
            return pd.DataFrame()

    def limpieza_datos(self, df):
        # ... tu lógica actual de limpieza ...
        df_limpio = df.copy()
        # (resto sin cambios)
        return df_limpio
