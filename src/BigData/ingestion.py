import requests
import sqlite3
import pandas as pd
import os

# Definir la URL de la API
API_URL = "https://www.fruityvice.com/api/fruit/all"

# Definir la ruta de la base de datos SQLite
DB_PATH = "src/BigData/static/db/ingestion.db"
CSV_PATH = "src/BigData/static/xlsx/ingestion.csv"

def obtener_datos_api():
    """Obtiene los datos de la API y los devuelve en formato JSON."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print(f"Error al obtener datos de la API: {error}")
        return []   

    
def crear_base_datos():
    print(f"Ruta de la base de datos: {DB_PATH}")

    """Crea la base de datos y la tabla si no existen."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS frutas (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                familia TEXT,
                orden TEXT,
                carbohidratos REAL,
                proteinas REAL,
                grasas REAL,
                calorias REAL,
                azucar REAL
            )
        ''')
        conn.commit()

def insertar_datos(datos):
    """Inserta los datos obtenidos en la base de datos."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for fruta in datos:
            cursor.execute('''
                INSERT INTO frutas (nombre, familia, orden, carbohidratos, proteinas, grasas, calorias, azucar)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                fruta["name"], 
                fruta["family"], 
                fruta["order"], 
                fruta["nutritions"]["carbohydrates"], 
                fruta["nutritions"]["protein"], 
                fruta["nutritions"]["fat"], 
                fruta["nutritions"]["calories"], 
                fruta["nutritions"]["sugar"]
            ))
        conn.commit()

def generar_csv():
    """Exporta los datos a un archivo CSV."""
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM frutas", conn)
        df.to_csv(CSV_PATH, index=False)
        print(f"Archivo CSV generado: {CSV_PATH}")

if __name__ == "__main__":
    crear_base_datos()
    datos = obtener_datos_api()
    if datos:
        insertar_datos(datos)
        generar_csv()
        print("Proceso de ingesta completado con éxito.")
    else:
        print("No se encontraron datos para insertar.")
