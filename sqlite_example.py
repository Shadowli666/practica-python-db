import sqlite3
DB_FILE = "mi_tienda.db"

try:
    # 1. Conectar a la base de datos
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # 2. Crear una tabla (si no existe)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    """)

    # 3. Insertar datos (evitando duplicados)
    cursor.execute("INSERT OR IGNORE INTO productos (id, nombre, precio, stock) VALUES (?, ?, ?, ?)",
                   (1, 'Laptop Pro', 1499.99, 10))
    cursor.execute("INSERT OR IGNORE INTO productos (id, nombre, precio, stock) VALUES (?, ?, ?, ?)",
                   (2, 'Mouse Inalámbrico', 24.50, 50))

    # 4. Confirmar los cambios en la base de datos
    conn.commit()
    print("Datos insertados o actualizados en SQLite.")

    # 5. Consultar y mostrar los datos
    print("\n--- Productos en la base de datos SQLite ---")
    cursor.execute("SELECT id, nombre, precio FROM productos")
    for producto in cursor.fetchall():
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

except sqlite3.Error as e:
    print(f"Error de SQLite: {e}")

finally:
    # 6. Cerrar la conexión
    if conn:
        conn.close()