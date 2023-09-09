import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl



def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    else:
        return text
    
#declaracion de la clase y propiedades del Homepage
class Homepage:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('SysVentas-Homepage')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("600x300")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,600,300)            
        
        logo =utl.leer_imagen("./imagenes/logo.png", (100, 100))

        #Parte izquierda del Homepage declarando un frame para el logo

        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=5, pady=5,bg='#3a7ff6')
        frame_logo.pack(side="left",expand=tk.NO, fill=tk.BOTH)               
        label = tk.Label( frame_logo, image=logo, bg='#3a7ff6' )
        label.place(x=0,y=-70, relwidth=1, relheight=1)
        
        label_text = "UserName"  # Tu texto aquí
        label_text = truncate_text(label_text, 15)

        frame_form_bottom = tk.Frame(frame_logo, bd=0, relief=tk.SOLID, bg='black')
        frame_form_bottom.pack(side="bottom",fill=tk.BOTH)
        title = tk.Label(frame_form_bottom, text=label_text, font=('Times', 20), fg="#fcfcfc",bg='#3a7ff6',pady=30)
        title.pack(expand=tk.NO)
    

        #Parte derecha del Homepage

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        frame_form_bottom = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_bottom.pack(side="bottom",fill=tk.X)
        title = tk.Label(frame_form_bottom, text="Inicio de sesión",font=('Times', 20), fg="#666a88",bg='#fcfcfc',pady=30)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        
       
        
        self.ventana.mainloop()