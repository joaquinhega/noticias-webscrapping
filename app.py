import csv
import requests
from bs4 import BeautifulSoup

def obtener_html(url):
    """ Obtiene el contenido HTML de una URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        respuesta = requests.get(url, headers=headers, timeout=10)
        
        if respuesta.status_code == 200:
            print("Página obtenida con éxito.")
            return respuesta.text
        else: 
            print(f"Error al obtener la página: {respuesta.status_code}")
            return None
    except Exception as e:
        print(f"Error en la solicitud: {e}")
        return None
    
def extraer_titulos_noticias(html):
    """ Extrae los titulos de noticias del HTML """
    
    soup = BeautifulSoup(html, 'html.parser')
    titulos = []
    
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        # Filtro para los que parecen de noticias
        if heading.text.strip() and len(heading.text.strip()) > 20:
            titulos.append(heading.text.strip())
            
    for elemento in soup.select('.title, .news-title, .headline, .article-title'):
        if elemento.text.strip() and elemento.text.strip() not in titulos:
            titulos.append(elemento.text.strip())
    return titulos

def extraer_articulos(html):
    """ Extrae la información del artículo """
    soup = BeautifulSoup(html, 'html.parser')
    
    articulos = []
    
    contenedores = soup.select('article, div[data-component="text-block"], [data-testid="card-text-wrapper"]')
    
    if not contenedores:
        contenedores = soup.find_all('article')

    for articulo_elem in contenedores:
        articulo = {}
        
        titulo_elem = (articulo_elem.find(['h1', 'h2', 'h3']) or soup.find('h1'))
        
        if titulo_elem:
            articulo['titulo'] = titulo_elem.get_text().strip()
        else:
            continue

        fecha_elem = articulo_elem.find('time') or soup.find('time')
        articulo['fecha'] = fecha_elem.get_text().strip() if fecha_elem else 'Fecha no disponible'
        
        resumen_elem = articulo_elem.find('p') or articulo_elem.select_one('div[data-component="text-block"] p')
        articulo['resumen'] = resumen_elem.get_text().strip() if resumen_elem else 'Sin resumen'

        # Evitar duplicados
        if articulo not in articulos:
            articulos.append(articulo)
    
    return articulos

def guardar_en_csv(datos, nombre_archivo):
    """ Guarda una lista de diccionarios en un CSV. """
    try:
        if not datos:
            print("No hay datos para guardar.")
            return False
        columnas = datos[0].keys()
        
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=columnas)
            writer.writeheader()
            writer.writerows(datos)
        
        print(f"Datos guardados en {nombre_archivo} con éxito.")
        return True
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")
        return False

def main():
    """ Funcion principal del programa."""
    print("=== Web Scraper basico de noticias ===")
    url = input("Ingrese la URL del sitio de noticias: ")
    
    print(f"Obteniendo contenido de la URL")
    html = obtener_html(url)
    
    if not html:
        print("No se pudo obtener el contenido HTML. Saliendo.")
        return
    print(" Contenido descargado con exito.")
    
    #Menu de opciones
    print("Seleccione la operacion a realizar:")
    print("1. Extraer titulos de noticias")
    print("2. Extraer articulos completos")
    
    opcion = input("Ingrese 1 o 2: ")
    
    if opcion == '1':
        titulos = extraer_titulos_noticias(html)
        
        print(f"Se encontraron {len(titulos)} titulos de noticias:")
        
        for i, titulo in enumerate(titulos, 1):
            print(f"{i}. {titulo}")
            
        if titulos and input("¿Desea guardar los titulos en un archivo CSV? (s/n): ").lower() == 's':
            datos = [{'numero': i, 'titulo': titulo} for i, titulo in enumerate(titulos, 1)]
            guardar_en_csv(datos, "titulos_noticias.csv")
            
    elif opcion == '2':
        articulos = extraer_articulos(html)
        
        print(f"Se encontraron {len(articulos)} articulos:")
        
        for i, articulo in enumerate(articulos, 1):
            print(f"{i}. Titulo: {articulo['titulo']}")
            print(f"   Fecha: {articulo['fecha']}")
            print(f"   Resumen: {articulo['resumen']}\n")
        
        if articulos and input("¿Desea guardar los articulos en un archivo CSV? (s/n): ").lower() == 's':
            guardar_en_csv(articulos, "articulos_noticias.csv")


if __name__ == "__main__":
    main()