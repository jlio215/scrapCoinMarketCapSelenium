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
        df_limpio = df.copy()

        # 1) Eliminar columnas innecesarias si existieran
        for drop_col in ['#', 'Last 7 Days']:
            if drop_col in df_limpio.columns:
                df_limpio.drop(columns=[drop_col], inplace=True)

        # 2) Quitar "Buy" de Name
        if 'Name' in df_limpio.columns:
            df_limpio['Name'] = df_limpio['Name'].str.replace('Buy', '', regex=False).str.strip()

        # 3) Intercambiar , y . en Price, Volume(24h) y Market Cap
        def swap_commas_dots(x: str) -> str:
            tmp = x.replace(',', '<TMP>').replace('.', ',')
            return tmp.replace('<TMP>', '.')
        
        for col in ['Price', 'Volume(24h)', 'Market Cap']:
            if col in df_limpio.columns:
                df_limpio[col] = df_limpio[col].astype(str).apply(swap_commas_dots)

        # 4) En Market Cap: eliminar todo hasta (e incluyendo) primera letra
        if 'Market Cap' in df_limpio.columns:
            def strip_prefix_to_letter(s: str) -> str:
                return re.sub(r'^[^A-Za-z]*[A-Za-z]', '', s)
            df_limpio['Market Cap'] = df_limpio['Market Cap'].astype(str).apply(strip_prefix_to_letter)

        # 5) En Volume(24h): tras el último punto, conservar sólo las 3 cifras siguientes
        if 'Volume(24h)' in df_limpio.columns:
            def trim_volume(s: str) -> str:
                idx = s.rfind('.')
                if idx != -1 and len(s) > idx + 4:
                    return s[:idx+4]
                return s
            df_limpio['Volume(24h)'] = df_limpio['Volume(24h)'].astype(str).apply(trim_volume)

        # 6) En Circulating Supply: tras la primera letra, insertar " of "
        if 'Circulating Supply' in df_limpio.columns:
            def annotate_supply(s: str) -> str:
                # buscar índice de la primera letra
                for i, ch in enumerate(s):
                    if ch.isalpha():
                        # dividir en hasta esa letra y resto
                        return s[:i+1] + ' of ' + s[i+1:]
                return s
            df_limpio['Circulating Supply'] = df_limpio['Circulating Supply'].astype(str).apply(annotate_supply)

        return df_limpio
