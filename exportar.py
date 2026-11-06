import sqlite3
import json

# Conectar a la base de datos SQLite del proyecto
conexion = sqlite3.connect('db.sqlite3')
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

# Obtener los nombres de todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

datos_totales = {}

for tabla in tablas:
    nombre_tabla = tabla['name']
    # Omitir tablas internas del sistema SQLite
    if nombre_tabla.startswith('sqlite_'):
        continue
        
    cursor.execute(f"SELECT * FROM {nombre_tabla};")
    filas = [dict(fila) for fila in cursor.fetchall()]
    datos_totales[nombre_tabla] = filas

# Guardar la estructura completa en un archivo JSON intermedio
with open('datos_sqlite.json', 'w', encoding='utf-8') as f:
    json.dump(datos_totales, f, ensure_ascii=False, indent=4)

conexion.close()
print("¡Exportación exitosa! Se ha creado el archivo datos_sqlite.json")