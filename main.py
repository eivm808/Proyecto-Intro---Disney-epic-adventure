# Proyecto 1 - Disney's Epic Adventure
# Introducción a la Programación - TEC



###########################################
#Importacion Tkinter y pillow             #
###########################################

import tkinter as tk
from PIL import Image, ImageTk



#############################################
#Ventana pricipal                           #
#############################################

root = tk.Tk()
root.geometry("1280x720")

root.title("Proyecto 01 Intro")


#############################################
#Imagen Fondo                               #
#############################################

ruta_imagen = "Assets\\Imagenes\\Fondos\\Menu freddy cabeza.png"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((1280,720))
imagen_tk = ImageTk.PhotoImage(imagen)

fondo = tk.Label(root, image=imagen_tk)
fondo.place(x=0, y=0)

#############################################
#Titulo del juego                           #
#############################################

titulo = tk.Label(root, text="Broken", font=('Times new roman',75), fg="#7d687d", bg="black")
titulo.place(x = 80, y = 100)
titulo2 = tk.Label(root, text="Circuits", font=('Times new roman',85), fg="#7d687d", bg="black")
titulo2.place(x = 80, y = 220)


#############################################
#Boton ABOUT                                #
#############################################


frame_about = tk.Frame(root, bg="white", bd=2, relief="solid")


tk.Label(frame_about, text="About Broken Circuits", font=("Arial", 16), fg="black", bg="white").pack()
tk.Label(frame_about, text="Estudiante: Ericka Villalobos", fg="black", bg="white").pack()
tk.Label(frame_about, text="Curso: Introducción a la Programación", fg="black", bg="white").pack()
tk.Label(frame_about, text="Profesor: Santiago Gamboa", fg="black", bg="white").pack()
tk.Label(frame_about, text="TEC - I Semestre 2026", fg="black", bg="white").pack()
tk.Button(frame_about, text="Cerrar", command=lambda: frame_about.place_forget()).pack(pady=5)


B1about = tk.Button(root, text='About', font='Arial', bg="Black",fg="white",
                    command=lambda:frame_about.place(x=60,y=450))
B1about.place(x=21, y=620)


#############################################
#Boton Play                                #
#############################################


botonStart = tk.Button(root, text='PLAY', bg="black",fg="white", )
botonStart.config(activebackground="black")
botonStart.place(x=80, y=400)

######################
#Ventana abierta     #
######################
root.mainloop()