import mysql.connector
from mysql.connector import Error

# --- La configuración se obtiene del entorno del Dev Container ---
DB_CONFIG = {
    "host": "db",  # <-- IMPORTANTE: Usar el nombre del servicio de Docker
    "user": "root",
    "password": "rootpassword", # La contraseña definida en docker-compose.yml
    "database": "python_practica_db"
}

try:
    # 1. Conectar a la base de datos que ya fue creada por Docker Compose
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Conexión a MySQL en Codespace exitosa.")

    # 2. Crear una tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            puesto VARCHAR(100)
        )
    """)

    # 3. Insertar datos (usa TRUNCATE para limpiar en cada ejecución de prueba)
    cursor.execute("TRUNCATE TABLE empleados")
    empleados = [('Ana Codespace', 'DevOps Engineer'), ('Carlos Cloud', 'DBA')]
    cursor.executemany("INSERT INTO empleados (nombre, puesto) VALUES (%s, %s)", empleados)
    conn.commit()
    print(f"{cursor.rowcount} empleados insertados en MySQL.")

    # 4. Consultar y mostrar los datos
    print("\n--- Empleados en MySQL ---")
    cursor.execute("SELECT * FROM empleados")
    for empleado in cursor.fetchall():
        print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Puesto: {empleado[2]}")

except Error as e:
    print(f"Error de MySQL: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nConexión a MySQL cerrada.")