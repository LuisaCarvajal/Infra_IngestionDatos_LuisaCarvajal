import requests
import json

def obtener_datos_api(url, fruta=None):
    """Consulta la API de Fruityvice.
    
    - Si se proporciona una fruta, devuelve los datos de esa fruta.
    - Si no se proporciona, devuelve la lista completa de frutas.
    """
    if fruta:
        url = f"{url}/{fruta}"  # Construye la URL con el nombre de la fruta
    else:
        url = f"{url}/all"  # Endpoint correcto para obtener todas las frutas
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error en la consulta: {error}")
        return {}

# URL base de la API
url_base = "https://www.fruityvice.com/api/fruit"

# Prueba con una fruta específica (ejemplo: "apple")
nombre_fruta = "Banana"  # Cambiar a "apple" u otra fruta si se desea
datos = obtener_datos_api(url_base, nombre_fruta)

# Imprimir resultados
if datos:
    print(json.dumps(datos, indent=4))
else:
    print("No se obtuvo información.")