import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Botón presionado!")
ventana = tk.Tk()         #Crea la ventana principal
ventana.title("Ventana simple") #le da un titulo

label = tk.Label(ventana, text="Presiona el boton para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack(pady=10)



ventana.mainloop()        #Muestra la ventana y espera acciones del usuario 
