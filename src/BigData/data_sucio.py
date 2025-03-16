import sqlite3
import random
import faker

# Inicializar Faker para generar nombres de frutas aleatorias
fake = faker.Faker()

# Ruta de la base de datos
DB_PATH = "src/BigData/static/db/ingestion.db"

# Conectar a la base de datos
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Listas de familias y órdenes de frutas simuladas
familias = ["Rosaceae", "Rutaceae", "Musaceae", "Fabaceae", "Solanaceae"]
ordenes = ["Rosales", "Sapindales", "Zingiberales", "Fabales", "Solanales"]

# Función para generar valores nulos aleatoriamente
def random_or_none(value, probability=0.1):
    return None if random.random() < probability else value

# Generar 150 registros sucios
datos_sucios = []
for _ in range(150):
    nombre = random_or_none(fake.word().capitalize(), probability=0.05)  # 5% nombres nulos
    familia = random.choice(familias)
    orden = random.choice(ordenes)
    carbohidratos = random_or_none(round(random.uniform(5, 30), 1), probability=0.1)  # 10% nulos
    proteinas = random_or_none(round(random.uniform(0.1, 5), 1), probability=0.1)
    grasas = random_or_none(round(random.uniform(0.1, 2), 1), probability=0.1)
    calorias = random_or_none(random.randint(30, 120), probability=0.05)
    azucar = random_or_none(round(random.uniform(1, 15), 1), probability=0.1)

    datos_sucios.append((nombre, familia, orden, carbohidratos, proteinas, grasas, calorias, azucar))

# Insertar los datos sucios en la base de datos
cursor.executemany('''
    INSERT INTO frutas (nombre, familia, orden, carbohidratos, proteinas, grasas, calorias, azucar) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', datos_sucios)

# Insertar registros duplicados (20 duplicados exactos)
for _ in range(20):
    datos_duplicados = random.choice(datos_sucios)
    cursor.execute('''
        INSERT INTO frutas (nombre, familia, orden, carbohidratos, proteinas, grasas, calorias, azucar) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', datos_duplicados)

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos ensuciada ")
