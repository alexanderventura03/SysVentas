import mysql.connector


conexion = mysql.connector.connect(host="sql10.freesqldatabase.com", database = "sql10645379", user="sql10645379", password="Fw9K2BszKr" )

def buscar_usuarios(email, password):
    cur = conexion.cursor();
    sql = "SELECT * FROM Usuarios_Admin WHERE email='"+email+"' AND Passwords = '"+password+"'";
    cur.execute(sql);
    usersx = cur.fetchall()
    cur.close()
    return usersx

