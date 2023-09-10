from tkinter import *
import tkinter as tk
from tkinter import ttk
import util.generic as utl
from data import conexion


def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    else:
        return text
    

class inventario:

    def __init__(self):        
        self.ventana = tk.Tk()                         
        self.ventana.title('SysVentas-Inventario')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500) 

         #Frames del inventario
        frame_botones = tk.Frame(self.ventana, bd=0, width=200, height = 75, relief=tk.SOLID, padx=5, pady=5,bg='#3a7ff6')
        frame_botones.pack(expand=tk.NO, fill=tk.BOTH) 
        frame_botones.pack_propagate(False) 

        frame_tabla = tk.Frame(self.ventana, width=800, height = 425, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_tabla.pack(expand=tk.NO,fill=tk.BOTH)
        frame_tabla.pack_propagate(False) 

        frame_filtro = tk.Frame(frame_tabla, width=800, height = 65, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_filtro.pack(expand=tk.NO,fill=tk.BOTH, padx=10, pady=10)

        frame_producto = tk.Frame(frame_tabla, width=800, height = 300, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_producto.pack(expand=tk.NO,fill=tk.BOTH)

        # frame_contenedor = tk.Frame(frame_form_derecho, height = 300, bd=0, relief=tk.SOLID, bg='green', padx=5, pady=5)
        # frame_contenedor.pack(fill=tk.BOTH)
        # frame_contenedor.place(x=0, y=0, relheight=1, relwidth=1)

         #Frame botones del Inventario

                      
        # label = tk.Label( frame_izquierdo, bg='#3a7ff6' )
        # label.place(x=0,y=-70, relwidth=1, relheight=1)
        
        # frame_izquierdo_contenedor = tk.Frame(frame_izquierdo, height=200, bd=0, relief=tk.SOLID, bg='#3a7ff6')
        # frame_izquierdo_contenedor.pack(side="bottom",fill=tk.BOTH)
        # frame_izquierdo_contenedor.place(x=0,y=0, relwidth=1, relheight=1)
       
        #Boton Regresar
        frame_button_regresar = tk.Frame(frame_botones,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_button_regresar.pack(side="top", fill=tk.NONE, padx=25, pady=15)
        frame_button_regresar.place(x=5,y=15)

        inicio = tk.Button(frame_button_regresar,text="Regresar",font=('Times', 15), bg='#fcfcfc', bd=0, fg="black", height=1, width=8)
        inicio.pack(fill=tk.X, padx=2, pady=2)        
        inicio.bind("<Return>", (lambda event: self.singout()))

        #Creacion del filtro
        etiqueta_filtro = tk.Label(frame_filtro, text="Filtrar", font=('Times', 14) ,fg="black",bg='#bae3f7', anchor="w")
        etiqueta_filtro.pack(fill=tk.X, padx=20,pady=5)
        self.filtro = ttk.Entry(frame_filtro, font=('Times', 14))
        self.filtro.pack(fill=tk.X, padx=20,pady=10)


       

        #creacion de la tabla en nuestra ventana con el paquete Treeview
        tv = ttk.Treeview(frame_producto)
        tv = ttk.Treeview(frame_producto, columns=("col1","col2","col3","col4","col5","col6"))
       
        tv.column("#0", width=40)
        tv.column("col1", width=150, anchor="center")
        tv.column("col2", width=130, anchor="center")
        tv.column("col3", width=70, anchor="center")
        tv.column("col4", width=70, anchor="center")
        tv.column("col5", width=165, anchor="center")
        tv.column("col6", width=120, anchor="center")

        tv.heading("#0",text="ID", anchor="center")
        tv.heading("col1",text="Nombre", anchor="center")
        tv.heading("col2",text="Categoria", anchor="center")
        tv.heading("col3",text="Precio", anchor="center")
        tv.heading("col4",text="Existencia", anchor="center")
        tv.heading("col5",text="Descripcion", anchor="center")
        tv.heading("col6",text="Fecha", anchor="center")


        productos = conexion.consultar_inventario()
        for producto in productos:
            tv.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))
        
        

        tv.pack(side="top", fill=tk.NONE, padx=25, pady=15)
        #tv.place(x=5,y=15)
        tv.pack_propagate(False)  

        self.ventana.mainloop()
