FROM python:3.9-slim

WORKDIR /scrapCoinMarketCapSelenium

# 1) Instala Chromium + Chromedriver y dependencias mínimas
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      chromium \
      chromium-driver \
      wget \
      curl \
      unzip \
      fonts-liberation \
      libnss3 \
      libxss1 \
      libasound2 \
      libatk-bridge2.0-0 \
      libgtk-3-0 \
      libx11-xcb1 \
      xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# 2) Copia tu código
COPY . .

# 3) Crea los directorios de output
RUN mkdir -p static/csv static/db

# 4) Instala dependencias de Python
RUN pip install --upgrade pip && \
    pip install -e . && \
    rm -rf /root/.cache/pip

# 5) Asegura que Selenium use Chromium
ENV PYTHONPATH=/scrapCoinMarketCapSelenium/src \
    CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver

# 6) Permite ejecutar cualquier script con: docker run contenedor python3 <script>
CMD ["python3"]
