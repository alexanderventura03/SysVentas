import mysql.connector

class Dao:
    def __init__(self):
        self.conexion = mysql.connector.connect(host="sql10.freesqldatabase.com", database="sql10645379", 
                                               user="sql10645379", password="Fw9K2BszKr")

    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT id_producto, Nombre_producto, precio, Cantidad_disponible FROM productos ORDER BY Nombre_producto ASC"
        cursor.execute(sql)
        productos = cursor.fetchall()
        cursor.close()
        return productos

    def buscar_usuarios(self, email, password):
        cur = self.conexion.cursor();
        sql = "SELECT * FROM Usuarios WHERE email='"+email+"' AND Contrasena = '"+password+"'";
        cur.execute(sql);
        usersx = cur.fetchall()
        cur.close()
        return usersx

