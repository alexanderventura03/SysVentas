import mysql.connector


conexion = mysql.connector.connect(host="127.0.0.1", database = "sysventasdb", user="root", password="" )

def buscar_usuarios(email, password):
    cur = conexion.cursor();
    sql = "SELECT * FROM usuarios_admin WHERE email='"+email+"' AND password = '"+password+"'";
    cur.execute(sql);
    usersx = cur.fetchall()
    cur.close()
    return usersx

