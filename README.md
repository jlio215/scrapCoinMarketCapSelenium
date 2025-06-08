# 🚀 CoinMarketCap Scraper con Selenium

[![Python](https://img.shields.io/badge/Python-3.9.2-blue.svg)](https://www.python.org/downloads/release/python-392/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://selenium-python.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI/CD](https://github.com/jlio215/scrapCoinMarketCapSelenium/workflows/CI/badge.svg)](https://github.com/jlio215/scrapCoinMarketCapSelenium/actions)

## 📖 Descripción

Este proyecto implementa un scraper automatizado para extraer datos de criptomonedas desde CoinMarketCap utilizando Selenium WebDriver. Forma parte de una guía completa de herramientas para web scraping y automatización, diseñada para enseñar desde la configuración del entorno hasta el despliegue de soluciones automatizadas.

## 🎯 Objetivos del Proyecto

- Extraer datos actualizados de criptomonedas (precio, capitalización, volumen, etc.)
- Automatizar el proceso de recolección de datos
- Implementar buenas prácticas de desarrollo y CI/CD
- Almacenar datos de forma estructurada para análisis posterior
- Monitorear y auditar el proceso de scraping


## 🛠️ Requisitos del Sistema

### Software necesario:
- **Python 3.9.2**
- **Visual Studio Code (VSCode)**
- **Git**
- **Chrome/Chromium** (para Selenium WebDriver)

### Librerías principales:
- `selenium>=4.0.0`
- `pandas>=1.3.0`
- `beautifulsoup4>=4.9.0`
- `requests>=2.25.0`
- `python-dotenv>=0.19.0`

## ⚙️ Instalación y Configuración

### 1. Configuración del entorno Python

#### Windows:
```bash
# Descargar Python 3.9.2 desde https://www.python.org/downloads/release/python-392/
# Asegúrate de marcar "Add Python 3.9 to PATH" durante la instalación

# Verificar instalación
python --version
pip --version
```

#### Linux/Mac:
```bash
# Instalar Python 3.9.2 usando pyenv (recomendado)
pyenv install 3.9.2
pyenv local 3.9.2

# Verificar instalación
python3 --version
pip3 --version
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/jlio215/scrapCoinMarketCapSelenium.git
cd scrapCoinMarketCapSelenium
```

### 3. Crear y activar entorno virtual

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Deberás ver `(venv)` al inicio de tu terminal, indicando que el entorno está activado.

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Configuración del scraper
COINMARKETCAP_URL=https://coinmarketcap.com/
DELAY_BETWEEN_REQUESTS=2
MAX_RETRIES=3
HEADLESS_MODE=true

# Configuración de base de datos
DATABASE_URL=sqlite:///data/crypto_data.db

# Configuración de logging
LOG_LEVEL=INFO
LOG_FILE=logs/scraper.log
```

## 🚀 Uso del Scraper

### Ejecución básica

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Ejecutar el scraper principal
python src/edu_pad/main.py
```

### Opciones de ejecución

```bash
# Scraping con parámetros específicos
python src/edu_pad/main.py --coins 100 --output csv --headless

# Scraping programado (cada hora)
python src/edu_pad/scheduler.py --interval 3600

# Modo debug
python src/edu_pad/main.py --debug --verbose
```

### Estructura de archivos del proyecto

```
scrapCoinMarketCapSelenium/
├── src/
│   └── edu_pad/
│       ├── main.py              # Orquestador principal
│       ├── scraper.py           # Lógica de scraping
│       ├── database.py          # Manejo de datos
│       └── utils.py             # Utilidades
├── data/                        # Datos extraídos
├── logs/                        # Archivos de log
├── tests/                       # Tests automatizados
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions
├── requirements.txt             # Dependencias
├── .env.example                # Plantilla de variables
└── README.md                   # Este archivo
```

## 📊 Datos Extraídos

El scraper recolecta la siguiente información para cada criptomoneda:

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `symbol` | Símbolo de la criptomoneda (BTC, ETH, etc.) | String |
| `name` | Nombre completo | String |
| `price` | Precio actual en USD | Float |
| `market_cap` | Capitalización de mercado | Float |
| `volume_24h` | Volumen de trading en 24h | Float |
| `change_24h` | Cambio porcentual en 24h | Float |
| `timestamp` | Fecha y hora de extracción | DateTime |

### Formatos de salida

- **CSV**: Para análisis en Excel/Google Sheets
- **JSON**: Para integración con APIs
- **SQLite**: Base de datos local para consultas SQL
- **Parquet**: Para análisis con pandas/Apache Spark

## 🔄 Automatización con GitHub Actions

El proyecto incluye workflows automatizados que se ejecutan:

- **CI/CD Pipeline**: En cada push y pull request
- **Data Validation**: Verificación de calidad de datos

### Configurar GitHub Actions

1. Habilita GitHub Actions en tu repositorio
2. Configura los secrets necesarios:
   - `DATABASE_URL`
   - `NOTIFICATION_WEBHOOK` (opcional)
3. Los workflows se ejecutarán automáticamente

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest tests/

# Tests con cobertura
pytest --cov=src tests/

# Tests específicos
pytest tests/test_scraper.py -v
```

## 📈 Monitoreo y Análisis

### Métricas clave monitoreadas:

- **Tiempo de ejecución** del scraper
- **Tasa de éxito** en las extracciones
- **Calidad de los datos** (completitud, consistencia)
- **Errores y excepciones**

### Dashboard de monitoreo

Accede al dashboard en: `http://localhost:8050` (después de ejecutar `python dashboard/app.py`)

## 🛡️ Consideraciones Éticas y Legales

- ✅ Respeta el `robots.txt` de CoinMarketCap
- ✅ Implementa delays apropiados entre requests
- ✅ No sobrecarga los servidores
- ✅ Cumple con los términos de servicio
- ✅ Uso exclusivamente educativo y de investigación

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📋 Roadmap

- [ ] Integración con más exchanges (Binance, Coinbase)
- [ ] API REST para consultar datos
- [ ] Dashboard web interactivo
- [ ] Alertas en tiempo real
- [ ] Machine Learning para predicciones
- [ ] Containerización con Docker

## ❓ Solución de Problemas

### Error: "chromedriver not found"
```bash
# Instalar webdriver-manager
pip install webdriver-manager

# O descargar manualmente desde:
# https://chromedriver.chromium.org/
```

### Error: "Permission denied" en Linux
```bash
chmod +x src/edu_pad/main.py
```

### Problemas con SSL
```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package>
```

## 📚 Recursos Adicionales

- [Documentación oficial de Selenium](https://selenium-python.readthedocs.io/)
- [Guía de BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python Web Scraping Cookbook](https://github.com/REMitchell/python-scraping)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 👥 Autores

- **Julian Gonzalez** - *Desarrollo inicial* - [@jlio215](https://github.com/jlio215)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- CoinMarketCap por proporcionar datos públicos de criptomonedas
- Comunidad de Python por las librerías utilizadas
- Estudiantes y colaboradores del curso

---

⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella!

## 📞 Contacto

- GitHub: [@jlio215](https://github.com/jlio215)
- Email: jliogdev@gmail.com

---

*Última actualización: Junio 2025*