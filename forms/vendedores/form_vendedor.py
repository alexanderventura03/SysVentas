from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from data.conexion import Dao


def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    else:
        return text
    

class inventario:

    datos = Dao()

    def btn_buscar(self, frame_producto, busqueda):
        resultados = self.datos.btn_buscar(busqueda)
        self.limpiar_lista(frame_producto)
        self.crear_tabla(frame_producto, resultados)
        return resultados
    
    def btn_regresar(self):
        respuesta = messagebox.askyesno("Confirmar", "¿Deseas cerrar sesión?")
        from forms.form_login import App
        self.ventana.destroy()
        App()
    
    def limpiar_lista(self, frame_producto):
        for widget in frame_producto.winfo_children():
            widget.destroy()
    
    def crear_tabla(self, frame_producto, resultados):
        self.lista = ttk.Treeview(frame_producto)
        self.lista = ttk.Treeview(frame_producto, columns=("col1","col2","col3","col4","col5","col6"))
       
        self.lista.column("#0", width=40)
        self.lista.column("col1", width=150, anchor="center")
        self.lista.column("col2", width=130, anchor="center")
        self.lista.column("col3", width=70, anchor="center")
        self.lista.column("col4", width=70, anchor="center")
        self.lista.column("col5", width=165, anchor="center")
        self.lista.column("col6", width=120, anchor="center")

        self.lista.heading("#0",text="ID", anchor="center")
        self.lista.heading("col1",text="Nombre", anchor="center")
        self.lista.heading("col2",text="Categoria", anchor="center")
        self.lista.heading("col3",text="Precio", anchor="center")
        self.lista.heading("col4",text="Existencia", anchor="center")
        self.lista.heading("col5",text="Descripcion", anchor="center")
        self.lista.heading("col6",text="Fecha", anchor="center")

        if(resultados == ""):
            productos = self.datos.consultar_inventario()
            for producto in productos:
                if producto[7] is None:
                    self.lista.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))
        else:
            for resultado in resultados:
                if resultado[7] is None:
                    self.lista.insert("", END, text=resultado[0], values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6]))

        self.lista.pack(side="top", fill=tk.NONE, padx=25, pady=15)
        self.lista.pack_propagate(False)  

    def obtener_fila(self, event, frame_producto):
        id =StringVar()
        nombre =StringVar()
        categoria =StringVar()
        precio =StringVar()
        existencia =StringVar()
        descripcion =StringVar()
        nombreFila= self.lista.identify_row(event.y)
        elemento = self.lista.item(self.lista.focus())
        i = elemento['text']
        n = elemento['values'][0]
        c = elemento['values'][1]
        p = elemento['values'][2]
        e = elemento['values'][3]
        d = elemento['values'][4]

        id.set(i)
        nombre.set(n)
        categoria.set(c)
        precio.set(p)
        existencia.set(e)
        descripcion.set(d)
        pop = Toplevel(self.ventana)
        pop.geometry("400x200")
        txt_nombre = Entry(pop,textvariable= nombre).place(x=40,y=40)
        txt_categoria = Entry(pop,textvariable= categoria).place(x=40,y=80)
        txt_precio = Entry(pop,textvariable= precio).place(x=40,y=120)
        txt_existencia = Entry(pop,textvariable= existencia).place(x=200,y=40)
        txt_descripcion = Entry(pop,textvariable= descripcion).place(x=200,y=80)

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

        frame_filtro = tk.Frame(frame_tabla, width=800, height = 25, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_filtro.pack(expand=tk.NO,fill=tk.X, padx=10)
        frame_tabla.pack_propagate(False) 

        frame_filtro_input = tk.Frame(frame_filtro, width=700, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_filtro_input.pack(side="left", expand=tk.YES,fill=tk.X, pady=10)
        frame_tabla.pack_propagate(False) 

        frame_filtro_boton = tk.Frame(frame_filtro, width=100, height = 65, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_filtro_boton.pack(side="right", expand=tk.NO,fill=tk.BOTH, padx=10, pady=10)

        frame_producto = tk.Frame(frame_tabla, width=800, height = 300, bd=0, relief=tk.SOLID, bg='#bae3f7')
        frame_producto.pack(expand=tk.NO,fill=tk.BOTH)

        #Boton cerrar seccion
        frame_button_regresar = tk.Frame(frame_botones,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_button_regresar.pack(side="left", fill=tk.NONE, padx=25, pady=15)
       

        regresar = tk.Button(frame_button_regresar,text="cerrar seccion",font=('Times', 14), bg='#fcfcfc', bd=0, fg="black", height=1, width=9, padx=7, pady=4, command= lambda: self.btn_regresar())
        regresar.pack(fill=tk.X, padx=2, pady=2)
        
        etiqueta_titulo = Label(frame_botones, text="Inventario", fg="white", bg='#3a7ff6', width=32,font=('Times', 30), padx=150, pady=10)
        etiqueta_titulo.pack(side="right")


#         #Creacion del filtro
        etiqueta_filtro = tk.Label(frame_filtro_input, text="Filtrar", font=('Times', 14) ,fg="black",bg='#bae3f7', anchor="w")
        etiqueta_filtro.pack(fill=tk.X, padx=20,pady=5)
        self.filtro = ttk.Entry(frame_filtro_input, font=('Times', 14), width=15)
        self.filtro.pack(fill=tk.X, padx=20)


#         #Creacion del boton para filtrar
        frame_button_buscar = tk.Frame(frame_filtro_boton, bd=1, relief=tk.SOLID)
        frame_button_buscar.pack(side="bottom", fill=tk.NONE)
        buscar = tk.Button(frame_button_buscar, text="Buscar",font=('Times', 15), bg='#fcfcfc', bd=0, fg="black", height=1, width=8, command= lambda: self.btn_buscar(frame_producto, self.filtro.get()))
        buscar.pack(fill=tk.X, padx=2, pady=2) 


        #creacion de la tabla en nuestra ventana con el paquete Treeview
        self.crear_tabla(frame_producto, "")
        

        self.ventana.mainloop()
