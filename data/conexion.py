import mysql.connector

class Dao():

    def __init__(self):
        self.conexion = mysql.connector.connect(host="127.0.0.1", database = "sysventasdb", user="root", password="" )

    def buscar_usuarios(self, email, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuarios_admin WHERE email='"+email+"' AND password = '"+password+"'";
        cur.execute(sql);
        usersx = cur.fetchall()
        cur.close()
        return usersx

