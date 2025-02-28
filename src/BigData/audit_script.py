import requests
import sqlite3
import pandas as pd
import json

# Definir rutas
API_URL = "https://www.fruityvice.com/api/fruit/all"
DB_PATH = "src/BigData/static/db/ingestion.db"
AUDIT_PATH = "src/BigData/static/auditoria/ingestion.txt"  # 🔹 Define la ruta correctamente

# Obtener datos de la API
def obtener_datos_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al obtener datos de la API: {error}")
        return []

# Leer datos de la API
data = obtener_datos_api()
count_api = len(data)
print(f"Registros obtenidos de la API: {count_api}")

# Leer datos desde SQLite
with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query("SELECT * FROM frutas", conn)
    count_db = len(df)

print(f"Registros en la base de datos: {count_db}")

# Comparar y generar archivo de auditoría
with open(AUDIT_PATH, "w") as file:
    file.write("Informe de Auditoría de Ingesta de Datos\n")
    file.write("="*40 + "\n")
    file.write(f"Registros obtenidos de la API: {count_api}\n")
    file.write(f"Registros en la base de datos: {count_db}\n")

    if count_api == count_db:
        file.write("La cantidad de registros coincide.\n")
    else:
        file.write(f"Diferencia en la cantidad de registros. {abs(count_api - count_db)}\n")

print(f"Archivo de auditoría generado en: {AUDIT_PATH}")
