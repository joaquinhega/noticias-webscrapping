# Web Scraper de Noticias

Un scraper web básico en Python para extraer información de sitios de noticias.

## Descripción

Este proyecto permite extraer títulos de noticias y artículos completos de sitios web, guardando los resultados en archivos CSV para su análisis posterior.

## Características

- Extracción de títulos de noticias
- Extracción de artículos completos (título, fecha, resumen)
- Exportación a formato CSV
- Headers personalizados para evitar bloqueos
- Manejo de errores y timeouts

## Requisitos

- Python 3.7+
- requests
- beautifulsoup4

## Instalación

1. Clona este repositorio:
```bash
git clone <tu-repositorio>
cd web_scrapper
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
```

3. Activa el entorno virtual:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta el script:
```bash
python app.py
```

2. Ingresa la URL del sitio de noticias que deseas scrapear

3. Selecciona la operación:
   - **Opción 1**: Extraer solo títulos de noticias
   - **Opción 2**: Extraer artículos completos (título, fecha, resumen)

4. Opcionalmente, guarda los resultados en un archivo CSV

## Ejemplo

```
=== Web Scraper basico de noticias ===
Ingrese la URL del sitio de noticias: https://ejemplo.com/noticias
Obteniendo contenido de la URL
Página obtenida con éxito.
Contenido descargado con exito.
Seleccione la operacion a realizar:
1. Extraer titulos de noticias
2. Extraer articulos completos
Ingrese 1 o 2: 2
```

## Estructura del Proyecto

```
web_scrapper/
├── app.py              # Script principal
├── .gitignore          # Archivos ignorados por git
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## Archivos Generados

- `titulos_noticias.csv`: Contiene los títulos extraídos
- `articulos_noticias.csv`: Contiene artículos completos (título, fecha, resumen)
