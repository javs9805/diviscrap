import sqlite3
from datetime import datetime
import os

class GestorBaseDeDatos:
    def __init__(self):
        self.db_name = "diviscrap.db"

    def __connect_to_database__(self):
        return sqlite3.connect(self.db_name)

    def create_database(self):
        conn = self.__connect_to_database__()
        c = conn.cursor()
        # Crear la tabla "Casa_de_cambios"
        c.execute('''
        CREATE TABLE IF NOT EXISTS Casa_de_cambios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ubicacion TEXT
        )
        ''')

        # Crear la tabla intermedia "Casa_de_cambios_Moneda"
        c.execute('''
        CREATE TABLE IF NOT EXISTS Casa_de_cambios_Moneda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            id_casa_de_cambios INTEGER,
            FOREIGN KEY (id_casa_de_cambios) REFERENCES Casa_de_cambios(id)
        )
        ''')

        # Crear la tabla "Moneda"
        c.execute('''
        CREATE TABLE IF NOT EXISTS Moneda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            compra REAL,
            venta REAL,
            timestamp DATETIME,
            id_casa_de_cambios_Moneda INTEGER,
            FOREIGN KEY (id_casa_de_cambios_Moneda) REFERENCES Casa_de_cambios_Moneda(id)
        )
        ''')

        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        print("Base de datos creada exitosamente.")

    def crear_casa_de_cambios(self, nombre, ubicacion=""):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Casa_de_cambios (nombre, ubicacion) VALUES (?, ?)", (nombre, ubicacion))
        conn.commit()
        conn.close()

    def leer_todas_las_casas_de_cambios(self):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Casa_de_cambios")
        casas_de_cambios = cursor.fetchall()
        conn.close()
        return casas_de_cambios

    def actualizar_casa_de_cambios(self, id, nombre, ubicacion):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("UPDATE Casa_de_cambios SET nombre = ?, ubicacion = ? WHERE id = ?", (nombre, ubicacion, id))
        conn.commit()
        conn.close()

    def eliminar_casa_de_cambios(self, id):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Casa_de_cambios WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def crear_moneda(self, nombre, compra, venta, timestamp, fkRelacion):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        timestamp = timestamp
        cursor.execute("INSERT INTO Moneda (nombre, compra, venta, timestamp, id_casa_de_cambios_Moneda) VALUES (?, ?, ?, ?, ?)", (nombre, compra, venta, timestamp, fkRelacion))
        conn.commit()
        conn.close()

    def leer_todas_las_monedas(self):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Moneda")
        monedas = cursor.fetchall()
        conn.close()
        return monedas

    def actualizar_moneda(self, id, nombre, compra, venta):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        timestamp = datetime.now()
        cursor.execute("UPDATE Moneda SET nombre = ?, compra = ?, venta = ?, timestamp = ? WHERE id = ?", (nombre, compra, venta, timestamp, id))
        conn.commit()
        conn.close()

    def eliminar_moneda(self, id):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Moneda WHERE id = ?", (id,))
        conn.commit()
        conn.close()
    
    def verificar_si_existe_en(self,tabla,columnas,valores):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()

        query = "SELECT * FROM {} WHERE ".format(tabla)
        condiciones = " AND ".join("{} = ?".format(col) for col in columnas)
        query += condiciones

        cursor.execute(query,valores)
        casas_de_cambios = cursor.fetchall()
        conn.close()
        return casas_de_cambios
    def crear_relacion_casa_moneda(self, nombre_casa, nombre_moneda):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        
        # Buscar el ID de la casa de cambios por su nombre
        cursor.execute("SELECT id FROM Casa_de_cambios WHERE nombre = ?", (nombre_casa,))
        casa_id = cursor.fetchone()
        if not casa_id:
            print("La casa de cambios no existe.")
            conn.close()
            return

        # Crear la relación en Casa_de_cambios_Moneda
        cursor.execute("INSERT INTO Casa_de_cambios_Moneda (nombre, id_casa_de_cambios, nombre) VALUES (?, ?, ?)", (nombre_moneda, casa_id[0], nombre_moneda))
        
        conn.commit()
        conn.close()

    def leer_todas_las_relaciones_casa_moneda(self):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Casa_de_cambios_Moneda")
        relaciones = cursor.fetchall()
        conn.close()
        return relaciones

    def eliminar_relacion_casa_moneda(self, id):
        conn = self.__connect_to_database__()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Casa_de_cambios_Moneda WHERE id = ?", (id,))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    gestor_db = GestorBaseDeDatos()
    print(gestor_db.create_database())
    #gestor_db.create_database()

