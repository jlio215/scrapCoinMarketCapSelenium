FROM python:3.9-slim

WORKDIR /scrapCoinMarketCapSelenium

# Instala Chrome y dependencias
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libappindicator1 \
    libindicator7 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Instalar Chrome (estable)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Instalar chromedriver automáticamente compatible
RUN CHROME_VERSION=$(google-chrome-stable --version | grep -oP '\d+\.\d+\.\d+') && \
    CHROMEDRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Instalar dependencias de Python
COPY . .

RUN mkdir -p static/csv static/db

RUN pip install --upgrade pip && \
    pip install -e . && \
    rm -rf /root/.cache/pip

ENV PYTHONPATH=/scrapCoinMarketCapSelenium/src

CMD ["python3"]
