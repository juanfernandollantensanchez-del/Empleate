import json
from pymongo import MongoClient

# Conexión al servidor local de MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['empleate_db_mongo']  # Nombre que tendrá tu base de datos en MongoDB

# Cargar el archivo JSON generado en el paso anterior
with open('datos_sqlite.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Iterar sobre cada tabla de SQLite y convertirla en una colección de MongoDB
for nombre_tabla, registros in datos.items():
    coleccion = db[nombre_tabla]
    coleccion.delete_many({})  # Limpiar duplicados si ya existían registros
    
    if registros:
        coleccion.insert_many(registros)
        print(f"Colección '{nombre_tabla}' importada con {len(registros)} documentos.")
    else:
        print(f"La tabla '{nombre_tabla}' estaba vacía.")

print("¡Migración a MongoDB completada con éxito!")