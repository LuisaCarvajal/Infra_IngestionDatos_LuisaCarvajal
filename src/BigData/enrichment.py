import requests
import pandas as pd

# Función para obtener todas las frutas de Fruityvice
def get_all_fruits():
    url = "https://www.fruityvice.com/api/fruit/all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Devuelve la lista completa de frutas
    except requests.exceptions.RequestException:
        return []

# Función para obtener datos nutricionales de TheMealDB
def get_themealdb_data(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={ingredient}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["meals"]:  # Si hay resultados, retorna el primero
            return data["meals"][0]
        else:
            return find_similar_meal(ingredient)  # Busca una alternativa
    except (requests.exceptions.RequestException, KeyError):
        return None

# Función para buscar una comida relacionada
def find_similar_meal(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["meals"]:
            meal_name = data["meals"][0]["strMeal"]
            return get_themealdb_data(meal_name)
    except (requests.exceptions.RequestException, KeyError):
        return None

# Obtener todas las frutas
fruits_data = get_all_fruits()

# Lista para almacenar datos combinados
merged_data = []

for fruit in fruits_data:
    fruit_name = fruit["name"]
    mealdb_data = get_themealdb_data(fruit_name)

    if mealdb_data:
        data_entry = {
            "Fruta": fruit_name,
            "Familia": fruit.get("family", "N/A"),
            "Orden": fruit.get("order", "N/A"),
            "Genus": fruit.get("genus", "N/A"),
            "Receta Relacionada": mealdb_data.get("strMeal", "No disponible"),
            "Instrucciones de Receta": mealdb_data.get("strInstructions", "No disponible")
        }
        merged_data.append(data_entry)

# Guardar los datos en CSV si hay datos disponibles
if merged_data:
    df = pd.DataFrame(merged_data)
    df.to_csv("src/BigData/static/xlsx/enriched_data.csv", index=False)

    # Generar el reporte en TXT
    with open("src/BigData/static/auditoria/enriched_report.txt", "w") as report:
        report.write("Reporte de Integración de Datos\n")
        report.write("=" * 40 + "\n")
        for item in merged_data:
            report.write(f"Fruta: {item['Fruta']}\n")
            report.write(f" - Familia: {item['Familia']}\n")
            report.write(f" - Orden: {item['Orden']}\n")
            report.write(f" - Genus: {item['Genus']}\n")
            report.write(f" - Receta Relacionada: {item['Receta Relacionada']}\n")
            report.write(f" - Instrucciones de Receta: {item['Instrucciones de Receta']}\n")
            report.write("=" * 40 + "\n")