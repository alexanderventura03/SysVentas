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
        sql = "SELECT * FROM Usuarios WHERE Email='"+email+"' AND Contrasena = '"+password+"'";
        cur.execute(sql);
        usersx = cur.fetchall()
        cur.close()
        return usersx
    
    def actualizar_inventario(self, id_producto, cantidad_a_eliminar):
        cursor = self.conexion.cursor()
        # Convierte las variables a cadenas utilizando str()
        id_producto_str = str(id_producto)
        cantidad_a_eliminar_str = str(cantidad_a_eliminar)
        
        # Usa parámetros en la consulta para evitar la concatenación
        sql = "UPDATE productos SET Cantidad_disponible = %s WHERE Id_producto = %s"
        
        cursor.execute(sql, (cantidad_a_eliminar_str, id_producto_str))
        self.conexion.commit()
        cursor.close()

    def insertar_factura(self, numero_factura, fecha_compra, sub_total, impuestos, total):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Facturas (numero_factura, fecha_compra, sub_total, impuestos, total) VALUES (%s, %s, %s, %s, %s)"
        valores = (numero_factura, fecha_compra, sub_total, impuestos, total)
        
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()

    def insertar_detalle_factura(self, numero_factura, nombre_producto, cantidad, costo_unitario, costo_total):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO DetalleFactura (numero_factura, nombre_producto, cantidad, costo_unitario, costo_total) VALUES (%s, %s, %s, %s, %s)"
        valores = (numero_factura, nombre_producto, cantidad, costo_unitario, costo_total)
        
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()

    def buscar_usuarios(self, email, password):
        cur = self.conexion.cursor();
        sql = "SELECT * FROM Usuarios WHERE Email='"+email+"' AND Contrasena = '"+password+"'";
        cur.execute(sql);
        usersx = cur.fetchall()
        cur.close()
        return usersx


    def consultar_inventario(self):
        cur = self.conexion.cursor();
        sql = "SELECT Id_producto, Nombre_producto, Categoria, Precio, Cantidad_disponible, Descripcion, Ultimo_Updated FROM productos";
        cur.execute(sql);
        products = cur.fetchall()
        cur.close()
        return products

    def btn_buscar(self, busqueda):
        cur = self.conexion.cursor();
        sql = "SELECT Id_producto, Nombre_producto, Categoria, Precio, Cantidad_disponible, Descripcion, Ultimo_Updated \
                FROM productos\
                WHERE Id_producto LIKE \'%"+busqueda+"%\'\
                OR Nombre_producto LIKE \'%"+busqueda+"%\'\
                OR Categoria LIKE \'%"+busqueda+"%\'\
                OR Precio LIKE \'%"+busqueda+"%\'\
                OR Cantidad_disponible LIKE \'%"+busqueda+"%\'\
                OR Descripcion LIKE \'%"+busqueda+"%\'\
                OR Ultimo_Updated LIKE \'%"+busqueda+"5%\'";
        cur.execute(sql);
        products = cur.fetchall()
        cur.close()
        return products

