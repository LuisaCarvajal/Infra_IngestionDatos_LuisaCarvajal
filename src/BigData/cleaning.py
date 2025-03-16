import pandas as pd
import sqlite3
import logging
import os

# Configuración de logging
LOG_PATH = "src/BigData/static/auditoria/cleaning_report.txt"
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Definir la ruta de la base de datos y archivo de salida
DB_PATH = "src/BigData/static/db/ingestion.db"
CLEANED_CSV_PATH = "src/BigData/static/xlsx/cleaned_data.csv"

# Cargar los datos desde la base de datos
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM frutas", conn)
conn.close()

# Análisis exploratorio inicial
initial_rows = df.shape[0]
null_values = df.isnull().sum().sum()
duplicates = df.duplicated(subset=['nombre', 'familia', 'orden', 'carbohidratos', 'proteinas', 'grasas', 'calorias', 'azucar']).sum()
logging.info(f"Registros iniciales: {initial_rows}")
logging.info(f"Valores nulos detectados: {null_values}")
logging.info(f"Registros duplicados: {duplicates}")

# Limpieza de datos
# 1. Eliminación de duplicados (ignorando el ID)
df = df.drop_duplicates(subset=['nombre', 'familia', 'orden', 'carbohidratos', 'proteinas', 'grasas', 'calorias', 'azucar'])

# 2. Manejo de valores nulos (imputación con la media en columnas numéricas)
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# 3. Corrección de tipos de datos (ejemplo: convertir nombres a formato título)
df['nombre'] = df['nombre'].str.title()

# Estadísticas post-limpieza
final_rows = df.shape[0]
logging.info(f"Registros después de la limpieza: {final_rows}")

# Guardar resultados
os.makedirs(os.path.dirname(CLEANED_CSV_PATH), exist_ok=True)
df.to_csv(CLEANED_CSV_PATH, index=False)
logging.info("Archivo cleaned_data.csv generado correctamente.")

print("Limpieza completada. Revisa cleaning_report.txt para detalles.")
