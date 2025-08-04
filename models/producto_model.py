import psycopg2
from psycopg2 import OperationalError
import time

class ProductoModel:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_config = {
            'dbname': db_name,
            'user': db_user,
            'password': db_password,
            'host': db_host,
            'port': db_port
        }
        self.conn = self._connect_db()
        self._create_table()

    def _connect_db(self):
        """Establece conexión con la base de datos PostgreSQL"""
        max_retries = 3
        retry_delay = 2
        
        for attempt in range(max_retries):
            try:
                conn = psycopg2.connect(**self.db_config)
                print("Conexión a la base de datos establecida")
                return conn
            except OperationalError as e:
                print(f"Intento {attempt + 1} de {max_retries} fallido")
                if attempt == max_retries - 1:
                    raise Exception(f"No se pudo conectar a la base de datos: {e}")
                time.sleep(retry_delay)

    def _create_table(self):
        """Crea la tabla productos si no existe"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT,
                    precio DECIMAL(10, 2) NOT NULL,
                    cantidad INTEGER NOT NULL,
                    categoria VARCHAR(50)
                )
            """)
            self.conn.commit()
        except Exception as e:
            raise Exception(f"No se pudo crear la tabla: {e}")

    def crear_producto(self, nombre, descripcion, precio, cantidad, categoria):
        """Crea un nuevo producto en la base de datos"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, descripcion, float(precio), int(cantidad), categoria))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"No se pudo crear el producto: {e}")

    def obtener_productos(self):
        """Obtiene todos los productos de la base de datos"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM productos ORDER BY id")
            return cursor.fetchall()
        except Exception as e:
            raise Exception(f"No se pudieron obtener los productos: {e}")

    def actualizar_producto(self, id_producto, nombre, descripcion, precio, cantidad, categoria):
        """Actualiza un producto existente"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE productos 
                SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s, categoria = %s
                WHERE id = %s
            """, (nombre, descripcion, float(precio), int(cantidad), categoria, int(id_producto)))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"No se pudo actualizar el producto: {e}")

    def eliminar_producto(self, id_producto):
        """Elimina un producto de la base de datos"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (int(id_producto),))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"No se pudo eliminar el producto: {e}")

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos"""
        if self.conn:
            self.conn.close()