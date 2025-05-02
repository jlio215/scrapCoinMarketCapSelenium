# Guía Completa de Herramientas para Web Scraping y Automatización

## Índice
- [Clase 1: Configuración del entorno de trabajo](#clase-1-configuración-del-entorno-de-trabajo-python-vscode-y-github)
- [Clase 2: Del problema al código](#clase-2-del-problema-al-código-ciclo-crisp-dm-y-primer-scrapper)
- [Clase 3: Scraping en acción I](#clase-3-scraping-en-acción-i-explorando-datos-con-beautifulsoup)
- [Clase 4: Scraping en acción II](#clase-4-scraping-en-acción-ii-selenium-scrapy-y-almacenamiento)
- [Clase 5: Automatiza tu desarrollo](#clase-5-automatiza-tu-desarrollo-fundamentos-de-integración-continua)
- [Clase 6: Diseñando flujos automatizados](#clase-6-diseñando-flujos-automatizados-con-github-actions)
- [Clase 7: Auditoría y monitoreo](#clase-7-auditoría-y-monitoreo-análisis-de-datos-y-prácticas-devops)
- [Clase 8: Cierre del curso](#clase-8-cierre-del-curso-tablero-bi-despliegue-y-casos-de-éxito)

## Clase 1: Configuración del entorno de trabajo: Python, VSCode y GitHub

### Herramientas necesarias
- Python 3.9.2
- Visual Studio Code (VSCode)
- Git
- GitHub

### Guía de instalación para Windows

#### 1. Instalación de Python 3.9.2
1. Descarga el instalador desde el [sitio oficial de Python 3.9.2](https://www.python.org/downloads/release/python-392/)
2. Ejecuta el instalador y marca la opción **"Add Python 3.9 to PATH"**
3. Selecciona **"Install Now"** para completar la instalación
4. Verifica la instalación abriendo CMD y ejecutando:
   ```
   python --version
   pip --version
   ```

#### 2. Configuración del entorno virtual
1. Abre CMD y navega hasta la carpeta donde deseas crear tu proyecto:
   ```
   cd C:\ruta\a\tu\proyecto
   ```
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   ```
   venv\Scripts\activate
   ```
4. Deberás ver `(venv)` al inicio de la línea de comandos, indicando que el entorno está activado

#### 3. Instalación de Visual Studio Code
1. Descarga VSCode desde el [sitio oficial](https://code.visualstudio.com/)
2. Instala siguiendo las instrucciones del asistente
3. Extensiones recomendadas:
   - Python (Microsoft)
   - Pylance
   - Git History
   - GitHub Pull Requests and Issues

#### 4. Instalación y configuración de Git
1. Descarga Git desde [git-scm.com](https://git-scm.com/download/win)
2. Instala siguiendo las instrucciones del asistente
3. Configura Git con tus credenciales:
   ```
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu@email.com"
   ```

#### 5. Configuración de GitHub
1. Crea una cuenta en [GitHub](https://github.com/)
2. Crea un nuevo repositorio para tu proyecto
3. Clona el repositorio en tu máquina local:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```

### Enlaces de documentación
- [Documentación oficial de Python 3.9.2](https://docs.python.org/3.9/)
- [Documentación de VSCode](https://code.visualstudio.com/docs)
- [Documentación de Git](https://git-scm.com/doc)
- [Documentación de GitHub](https://docs.github.com/es)

## Clase 2: Del problema al código: ciclo CRISP-DM y primer scrapper

### Herramientas necesarias
- Jupyter Notebook
- Google Colab
- Requests
- BeautifulSoup

### Guía de instalación y configuración

#### 1. Instalación de Jupyter Notebook (en tu entorno virtual)
1. Con el entorno virtual activado, instala Jupyter:
   ```
   pip install notebook
   ```
2. Inicia Jupyter Notebook:
   ```
   jupyter notebook