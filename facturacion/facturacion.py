from decimal import Decimal
from tkinter import *
from data.conexion import Dao
import random
import datetime
from tkinter import filedialog, messagebox
import string
from util.generic import centrar_ventana

# Inicializar la aplicación Tkinter
aplicacion = Tk()
aplicacion.geometry('1000x612+0+0')
aplicacion.title("SysVentas")
aplicacion.config(bg='#0369a1')
aplicacion.resizable(0,0);
centrar_ventana(aplicacion, 1000, 612)

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

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def resetear():
    texto_recibo.delete(0.1, END)
    visor_calculadora.delete(0, END)

    for texto in texto_producto:
        texto.set('0')

    for cuadro in cuadros_productos:
        cuadro.config(state=DISABLED)

    for p in productos_agregados:
        p.set(0)

    var_sub_total.set('')
    var_impuesto.set('')
    var_total.set('')


def recibo():
    # Caracteres permitidos (letras mayúsculas y dígitos)
    caracteres_permitidos = string.ascii_uppercase + string.digits
    total()
    id_generado = ''.join(random.choice(caracteres_permitidos) for _ in range(8))
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {id_generado}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'

    # Generar modelo factura
    factura.append([id_generado, fecha, Decimal(var_sub_total.get()), (Decimal(var_impuesto.get())), Decimal(var_total.get())])

    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 54 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for producto in texto_producto:
        if producto.get() != '0':
            texto_recibo.insert(END, f'{productos[x][1]}\t\t{producto.get()}\t'
                                     f'$ {Decimal(producto.get()) * productos[x][2]}\n')
            
            # Esto traerá el id y la cantidad que quedaría en la base de datos
            productos_actualizar.append([productos[x][0], int(productos[x][3]) - int(producto.get())])

            
            detalle_factura.append([id_generado, productos[x][1], Decimal(producto.get()), Decimal(productos[x][2]), (Decimal(productos[x][2]) * (Decimal(producto.get())))])
            
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')

    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_sub_total.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 54 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

def guardar_recibo():

    i = 0
    informacion_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=(".txt")) 
    archivo.write(informacion_recibo)
    archivo.close()

    for producto in productos_actualizar:
        datos.actualizar_inventario(producto[0], producto[1])

    datos.insertar_factura(factura[0][0], factura[0][1], factura[0][2], factura[0][3], factura[0][4])

    # Insertar los detalles de factura en la base de datos
    index = 0
    for detalle in detalle_factura:
        datos.insertar_detalle_factura(detalle[0], detalle[1], detalle[2], detalle[3], detalle[4],)
     
        index+=1

    factura.clear()
    detalle_factura.clear()

    messagebox.showinfo("Información", "Factura guardada correctamente")
# Crear un frame superior
panel_superior = Frame(aplicacion, bd=1, relief="flat")
panel_superior.pack(side="top")

etiqueta_titulo = Label(panel_superior, text="Sistema De Facturación", fg="white", bg='#0369a1', width=26,
                     font=("Times, 50"))
etiqueta_titulo.grid(row=0, column=0)

# Crear un frame izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief="solid")
panel_izquierdo.pack(side="left")

# Crear panel para costos
panel_coste = Frame(panel_izquierdo, bd=1, relief="flat", bg='#0369a1', padx=154)
panel_coste.pack(side="bottom")

# Crear un frame derecho
panel_derecho = Frame(aplicacion, bd=1, relief="flat")
panel_derecho.pack(side="right")

# Crear un frame para los productos (dentro del panel izquierdo)
panel_productos = LabelFrame(panel_izquierdo, text="Productos", font=("Dosis", 19, "bold"),
                             bd=1, relief="flat", fg="#3b82f6")
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
panel_calculadora = Frame(panel_derecho, bd=1, relief="flat", bg='#0369a1')
panel_calculadora.pack()

# Crear un frame para el recibo (dentro del panel derecho)
panel_recibo = Frame(panel_derecho, bd=1, relief="flat", bg='#0369a1')
panel_recibo.pack()

# Crear un frame para los botones (dentro del panel derecho)
panel_botones = Frame(panel_derecho, bd=1, relief="flat", bg='#0369a1')
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
                                       fg="#0c4a6e",
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
                                bg='#0369a1',
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
                                bg='#0369a1',
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
                                bg='#0369a1',
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
                   bg='#0369a1',
                   bd=1,
                   width=9)
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=13)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='#0369a1',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# Evitar que la aplicación se cierre
aplicacion.mainloop()