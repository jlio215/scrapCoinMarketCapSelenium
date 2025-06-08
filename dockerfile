FROM python:3.9-slim

WORKDIR /scrapCoinMarketCapSelenium

COPY . .

RUN mkdir -p static/csv static/db

RUN pip install --upgrade pip \
    && pip install -e . \
    && rm -rf /root/.cache/pip

ENV PYTHONPATH=/scrapCoinMarketCapSelenium/src

CMD ["python3"]
