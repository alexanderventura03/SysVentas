from decimal import Decimal
from tkinter import *
from data.conexion import Dao

# Inicializar la aplicación Tkinter
aplicacion = Tk()
aplicacion.geometry('1000x610+0+0')
aplicacion.title("SysVentas")
aplicacion.config(bg="burlywood")
aplicacion.resizable(0,0);

datos = Dao()

# variables
operador = ''
var_sub_total = StringVar()
var_impuesto = StringVar()
var_total = StringVar()
productos_actualizar = []
factura = []
detalle_factura = []

def revisar_check():
    x = 0
    for c in cuadros_productos:
        if(productos_agregados[x].get() == 1):
            cuadros_productos[x].config(state=NORMAL)
            if(productos_agregados[x].get() == 0):
                cuadros_productos[x].delete(0, END)
            cuadros_productos[x].focus()
        else:
            cuadros_productos[x].config(state=DISABLED)
            texto_producto[x].set('0')
        x+=1

def total():
    sub_total_producto = 0
    index = 0

    for cantidad in texto_producto:
        sub_total_producto = sub_total_producto + (Decimal(cantidad.get()) * productos[index][2])

        index += 1

    impuestos = sub_total_producto * Decimal(0.18)
    total = sub_total_producto + impuestos
    
    # Asignamos los valores a sus respectivos entrys
    var_sub_total.set(f"{round(sub_total_producto, 2)}")
    var_impuesto.set(f"{round(impuestos, 2)}")
    var_total.set(f"{round(total, 2)}")

# Crear un frame superior
panel_superior = Frame(aplicacion, bd=1, relief="flat")
panel_superior.pack(side="top")

etiqueta_titulo = Label(panel_superior, text="SysVentas", fg="azure4", bg="burlywood", width=27,
                     font=("Arial, 50"))
etiqueta_titulo.grid(row=0, column=0)

# Crear un frame izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief="flat")
panel_izquierdo.pack(side="left")

# Crear panel para costos
panel_coste = Frame(panel_izquierdo, bd=1, relief="flat", bg="azure4", padx=154)
panel_coste.pack(side="bottom")

# Crear un frame derecho
panel_derecho = Frame(aplicacion, bd=1, relief="flat")
panel_derecho.pack(side="right")

# Crear un frame para los productos (dentro del panel izquierdo)
panel_productos = LabelFrame(panel_izquierdo, text="Productos", font=("Dosis", 19, "bold"),
                             bd=1, relief="flat", fg="azure4")
panel_productos.pack(side="left")

# Crear un ScrolledFrame para la lista de productos
scrolled_frame = Frame(panel_productos)
scrolled_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(N, S, E, W))

# Crear una función para hacer scroll en el frame interno
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(scrolled_frame)
canvas.grid(row=0, column=0, sticky=(N, S, E, W))

# Scrollbar vertical
scrollbar_y = Scrollbar(scrolled_frame, orient="vertical", command=canvas.yview)
scrollbar_y.grid(row=0, column=1, sticky=(N, S))
canvas.configure(yscrollcommand=scrollbar_y.set)

# Scrollbar horizontal
scrollbar_x = Scrollbar(scrolled_frame, orient="horizontal", command=canvas.xview)
scrollbar_x.grid(row=1, column=0, sticky=(E, W))
canvas.configure(xscrollcommand=scrollbar_x.set)

frame_products = Frame(canvas)
canvas.create_window((0, 0), window=frame_products, anchor="nw")
frame_products.bind("<Configure>", on_frame_configure)

# Crear un frame para la calculadora (dentro del panel derecho)
panel_calculadora = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_calculadora.pack()

# Crear un frame para el recibo (dentro del panel derecho)
panel_recibo = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_recibo.pack()

# Crear un frame para los botones (dentro del panel derecho)
panel_botones = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_botones.pack()


# Productos orden en lista 0-ID, 1-Nombre Producto, 2-Precio, 3-Cantidad disponible
productos = datos.buscar_productos()

contador_fila = 0
contador_productos = 0
productos_agregados = []
cuadros_productos = []
texto_producto = []

for producto in productos:
    # Crear los checkbox
    productos_agregados.append(IntVar())
    producto_checkbutton = Checkbutton(frame_products, text=f"{producto[1]} - D:{producto[3]} - ${producto[2]}",
                                       font=("Dosis", 19, "bold"),
                                       variable=productos_agregados[contador_productos],
                                       command=revisar_check)
    producto_checkbutton.grid(row=contador_fila, column=0, sticky=W)


    # Crear los cuadros de entrada
    cuadros_productos.append('')
    texto_producto.append('')
    texto_producto[contador_productos] = StringVar()
    texto_producto[contador_productos].set('0')
    cuadros_productos[contador_productos] = Entry(frame_products, bd=1, 
                                                  font=('Dosis', 18, 'bold'),
                                                  width=6,
                                                  state=DISABLED,
                                                  textvariable=texto_producto[contador_productos]
                                                  )
    cuadros_productos[contador_productos].grid(row=contador_fila, column=1, padx=(10, 0))

    contador_productos += 1
    contador_fila += 1

canvas.config(scrollregion=canvas.bbox("all"), width=500, height=360)

etiqueta_sub_total = Label(panel_coste, text="Sub total: ", 
                                font=("Dosis", 12, "bold"),
                                bg="azure4",
                                fg="white",
                                padx=65,)

etiqueta_sub_total.grid(row=0, column=0)

texto_sub_total = Entry(panel_coste, 
                                font=("Dosis", 12, "bold"),
                                bd=1,
                                width=10,
                                state="readonly",
                                textvariable=var_sub_total)

texto_sub_total.grid(row=0, column=1)

etiqueta_impuesto = Label(panel_coste, text="Impuestos: ", 
                                font=("Dosis", 12, "bold"),
                                bg="azure4",
                                fg="white",
                                padx=60,)

etiqueta_impuesto.grid(row=1, column=0)

texto_impuesto = Entry(panel_coste, 
                                font=("Dosis", 12, "bold"),
                                bd=1,
                                width=10,
                                state="readonly",
                                textvariable=var_impuesto)

texto_impuesto.grid(row=1, column=1)

etiqueta_total = Label(panel_coste, text="      Total:     ", 
                                font=("Dosis", 12, "bold"),
                                bg="azure4",
                                fg="white",
                                padx=41,)

etiqueta_total.grid(row=2, column=0)

texto_total = Entry(panel_coste, 
                                font=("Dosis", 12, "bold"),
                                bd=1,
                                width=10,
                                state="readonly",
                                textvariable=var_total)

texto_total.grid(row=2, column=1)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=13)
texto_recibo.grid(row=0,
                  column=0)

# Evitar que la aplicación se cierre
aplicacion.mainloop()