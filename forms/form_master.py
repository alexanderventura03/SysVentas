import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import util.generic as utl



def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    else:
        return text
    
#declaracion de la clase y propiedades del Homepage
class Homepage:

    def signout(self):
        from forms.form_login import App
        respuesta = messagebox.askyesno("Confirmar", "¿Deseas cerrar la sesión?")
        if respuesta:
            self.ventana.destroy()
            App()
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                         
        self.ventana.title('SysVentas-Homepage')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("600x300")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,600,300)            
        
        logo =utl.leer_imagen("./imagenes/logo.png", (100, 100))

        #Frame izquierdo del Homepage 

        frame_izquierdo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=5, pady=5,bg='#3a7ff6')
        frame_izquierdo.pack(side="left",expand=tk.NO, fill=tk.BOTH) 
        frame_izquierdo.pack_propagate(False)               
        label = tk.Label( frame_izquierdo, image=logo, bg='#3a7ff6' )
        label.place(x=0,y=-70, relwidth=1, relheight=1)
        
        label_user_name = "UserName"  # Tu texto aquí
        label_user_name = truncate_text(label_user_name, 15)
        frame_izquierdo_contenedor = tk.Frame(frame_izquierdo, height=200, bd=0, relief=tk.SOLID, bg='#3a7ff6')
        frame_izquierdo_contenedor.pack(side="bottom",fill=tk.BOTH)
        frame_izquierdo_contenedor.place(x=0,y=130, relwidth=1, relheight=1)
        title = tk.Label(frame_izquierdo_contenedor, text=label_user_name, font=('Times', 20), fg="#fcfcfc",bg='#3a7ff6',pady=2)
        title.pack(expand=tk.NO, pady=15)

        #Boton Sign out
        frame_button_signout = tk.Frame(frame_izquierdo_contenedor,  bd=0, relief=tk.SOLID,bg='#fcfcfc') #fill significa llenar
        frame_button_signout.pack(side="top", fill=tk.NONE, padx=25)

        inicio = tk.Button(frame_button_signout,text="Sign out",font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg="black", height=1, width=8, command=self.signout)
        inicio.pack(fill=tk.X, padx=2, pady=2)        
        inicio.bind("<Return>", (lambda event: self.singout()))


        #Frame derecho del Homepage

        frame_form_derecho = tk.Frame(self.ventana, width=400, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_derecho.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        frame_derecho_contenedor = tk.Frame(frame_form_derecho, height = 300, bd=0, relief=tk.SOLID, bg='#666a88', padx=5, pady=5)
        frame_derecho_contenedor.pack(fill=tk.BOTH)
        frame_derecho_contenedor.place(x=0, y=0, relheight=1, relwidth=1)

        #Titulo de la vista
        frame_titulo_contenedor = tk.Frame(frame_derecho_contenedor, height=50, bd=0, relief=tk.SOLID, bg='#666a88', padx=5, pady=5)
        frame_titulo_contenedor.pack(side="top", fill=tk.BOTH)
        title = tk.Label(frame_titulo_contenedor, text="Página de inicio", font=('Times', 20), fg="black",bg='#cccccc',pady=10)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        #Contenedores de botones
        frame_derecho_botones1 = tk.Frame(frame_derecho_contenedor, height = 50, bd=0, relief=tk.SOLID, padx=10, bg='#666a88')
        frame_derecho_botones1.pack(side="top", fill=tk.BOTH, pady=45)
        frame_derecho_botones2 = tk.Frame(frame_derecho_contenedor, height = 50, bd=0, relief=tk.SOLID, padx=10, bg='#666a88')
        frame_derecho_botones2.pack(side="top", fill=tk.BOTH)

        #Boton agregar producto
        frame_button_agregar = tk.Frame(frame_derecho_botones1, bd=1, relief=tk.SOLID)
        frame_button_agregar.pack(side="left", fill=tk.NONE, padx=3)

        agregar = tk.Button(frame_button_agregar,text="Agregar Producto",font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg="black", width=14)
        agregar.pack(fill=tk.X, padx=2,pady=2)

        #Boton Consultar inventario
        frame_button_consulta = tk.Frame(frame_derecho_botones1, bd=1, relief=tk.SOLID)
        frame_button_consulta.pack(side="left", fill=tk.NONE, padx=3)

        consultar = tk.Button(frame_button_consulta,text="Consultar Productos",font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg="black", width=14)
        consultar.pack(fill=tk.X, padx=2, pady=2)
       
       #Boton Crear Factura
        frame_button_factura = tk.Frame(frame_derecho_botones2, bd=1, relief=tk.SOLID)
        frame_button_factura.pack(side="left", fill=tk.NONE, padx=3)

        facturar = tk.Button(frame_button_factura,text="Crear Factura", font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg="black", width=14)
        facturar.pack(fill=tk.X, padx=2,pady=2)
       
       #Boton Consultar Facturas
        frame_button_historial = tk.Frame(frame_derecho_botones2, bd=1, relief=tk.SOLID)
        frame_button_historial.pack(side="left", fill=tk.NONE, padx=3)

        historial = tk.Button(frame_button_historial,text="Consultar Facturas", font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg="black", width=14)
        historial.pack(fill=tk.X, padx=2,pady=2)
        
        self.ventana.mainloop()