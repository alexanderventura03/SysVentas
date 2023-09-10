import mysql.connector


conexion = mysql.connector.connect(host="sql10.freesqldatabase.com", database = "sql10645379", user="sql10645379", password="Fw9K2BszKr" )

def buscar_usuarios(email, password):
    cur = conexion.cursor();
    sql = "SELECT * FROM Usuarios WHERE Email='"+email+"' AND Contrasena = '"+password+"'";
    cur.execute(sql);
    usersx = cur.fetchall()
    cur.close()
    return usersx

def consultar_inventario():
    cur = conexion.cursor();
    sql = "SELECT Id_producto, Nombre_producto, Categoria, Precio, Cantidad_disponible, Descripcion, Ultimo_Updated FROM productos";
    cur.execute(sql);
    products = cur.fetchall()
    cur.close()
    return products

