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

frame_menu = tk.Frame(root, width=1280, height=720)
frame_menu.place(x=0, y=0)

root.title("Proyecto 01 Intro")
root.geometry("1280x720")


#############################################
#Imagen Fondo                               #
#############################################

ruta_fondomenu = "Assets\\Imagenes\\Fondos\\Menu freddy cabeza.png"
fondomenu = Image.open(ruta_fondomenu)
fondomenu = fondomenu.resize((1280,720))
fondomenu_tk = ImageTk.PhotoImage(fondomenu)

fondo = tk.Label(frame_menu, image=fondomenu_tk)
fondo.place(x=0, y=0)

#############################################
#Titulo del juego                           #
#############################################

titulo = tk.Label(frame_menu, text="Broken", font=('Times new roman',75), fg="#7d687d", bg="black")
titulo.place(x = 80, y = 100)
titulo2 = tk.Label(frame_menu, text="Circuits", font=('Times new roman',85), fg="#7d687d", bg="black")
titulo2.place(x = 80, y = 220)


#############################################
#Boton ABOUT y entry de nombre              #
#############################################

#frame con la info

frame_about = tk.Frame(frame_menu, bg="white", bd=2, relief="solid")

#texto y boton cerrar

tk.Label(frame_about, text="About Broken Circuits", font=("Arial", 16), fg="black", bg="white").pack()
tk.Label(frame_about, text="Estudiante: Ericka Villalobos", fg="black", bg="white").pack()
tk.Label(frame_about, text="Curso: Introducción a la Programación", fg="black", bg="white").pack()
tk.Label(frame_about, text="Profesor: Santiago Gamboa", fg="black", bg="white").pack()
tk.Label(frame_about, text="TEC - I Semestre 2026", fg="black", bg="white").pack()
tk.Button(frame_about, text="Cerrar", command=lambda: frame_about.place_forget()).pack(pady=5)

#boton play

B1about = tk.Button(frame_menu, text='About', font='Arial', bg="Black",fg="white",
                    command=lambda:frame_about.place(x=1060,y=450))
B1about.config(activebackground="black")
B1about.config(activeforeground="white")
B1about.place(x=1180, y=620)

#Entry nombre

nombre_jugador = tk.StringVar()

label_nombre = tk.Label(frame_menu, text="Ingrese su nombre", font=("Arial", 14), bg="black", fg="white")
label_nombre.place(x=80, y=370)
label_nombre.lift()

entry_nombre = tk.Entry(frame_menu, textvariable = nombre_jugador, font=("Arial", 14))
entry_nombre.place(x=80, y=400)

#############################################
#Ir a avatares                          #
#############################################

###Cambio a frame de avatares y entry nombre###

frame_avatares = tk.Frame(root, width = 1280, height=720, bg="black")

def ir_a_avatares():
    if nombre_jugador.get() == "":
        tk.Label(frame_menu, text="Ingresa tu nombre!", fg="red", bg="black").place(x=80, y=430)
    else:   
        frame_menu.forget()
        frame_avatares.place(x=0, y=0)

#fondo avatares 

ruta_fondo_avatares = "Assets\\Imagenes\\Fondos\\il (1).png"
fondo_avatares = Image.open(ruta_fondo_avatares)
fondo_personajes = fondo_avatares.resize((1280,720))
fondo_avatares_tk = ImageTk.PhotoImage(fondo_avatares)

fondo = tk.Label(frame_avatares, image=fondo_avatares_tk)
fondo.place(x=0, y=0)

#Boton play

botonStart = tk.Button(frame_menu, text='PLAY', font=("Arial", 12), bg="black",fg="white", width=20, height=2, relief="flat", command=ir_a_avatares)
botonStart.config(activebackground="black")
botonStart.config(activeforeground="white")
botonStart.place(x=80, y=480)


#############################################
#Seleccion de personajes                    #
#############################################

###FUNCIONES DE PERSONAJES###

def elegir_avatar(avatar_img):
    global avatar_seleccionado
    avatar_seleccionado = avatar_img
    frame_avatares.place_forget()
    frame_personajes.place(x=0, y=0)


###Botones imagenes de personajes###

#AVATAR 1: PHONE GUY
ruta_foto_phoneguy = "Assets\\Imagenes\\Avatares\\phoneguy.jpeg"
foto_phoneguy = Image.open(ruta_foto_phoneguy)
foto_avatar1 = foto_phoneguy.resize((300,300))
foto_phoneguy_tk = ImageTk.PhotoImage(foto_avatar1)

phone_guy= tk.Button(frame_avatares, image=foto_phoneguy_tk, bd=0, relief="flat",
                     command=lambda: elegir_avatar(foto_phoneguy_tk))
phone_guy.place(x=85, y=220)

#AVATAR 2: HELPY
ruta_foto_helpy = "Assets\\Imagenes\\Avatares\\helpy.jpeg"
foto_helpy = Image.open(ruta_foto_helpy)
foto_avatar2 = foto_helpy.resize((300,300))
foto_helpy_tk = ImageTk.PhotoImage(foto_avatar2)

helpy = tk.Button(frame_avatares, image=foto_helpy_tk, bd=0, relief="flat",
                  command=lambda: elegir_avatar(foto_helpy_tk))
helpy.place(x=500, y=240)

#AVATAR 3: MICHAEL AFTON
ruta_foto_MAF = "Assets\\Imagenes\\Avatares\\Michael.jpeg"
foto_MAF = Image.open(ruta_foto_MAF)
foto_avatar3 = foto_MAF.resize((300,300))
foto_MAF_tk = ImageTk.PhotoImage(foto_avatar3)

Michael = tk.Button(frame_avatares, image=foto_MAF_tk, bd=0, relief="flat",
                    command=lambda: elegir_avatar(foto_MAF_tk))
Michael.place(x=920, y=220)



#############################################
#Frame y seleccion de personajes            #
#############################################

frame_personajes = tk.Frame(root, width = 1280, height=720, bg="black")

ruta_fondo_personajes = "Assets\\Imagenes\\Fondos\\Fondo personajes.png"
fondo_personajes = Image.open(ruta_fondo_personajes)
fondo_personajes = fondo_personajes.resize((1280,720))
fondo_personajes_tk = ImageTk.PhotoImage(fondo_personajes)

fondo = tk.Label(frame_personajes, image=fondo_personajes_tk)
fondo.place(x=0, y=0)

#############################################
#Mapa y seleccion de nivel                  #
#############################################

#frame_mapa = tk.Frame(root, width = 1280, height=720, bg="black")

#ruta_fondo_mapa = "Assets\\Imagenes\\Mapa\\il (1).png"
#fondo_avatares = Image.open(ruta_fondo_avatares)
#fondo_personajes = fondo_avatares.resize((1280,720))
#fondo_avatares_tk = ImageTk.PhotoImage(fondo_avatares)

#fondo = tk.Label(frame_avatares, image=fondo_avatares_tk)
#fondo.place(x=0, y=0)

#def ir_a_mapa():
        #frame_avatares.forget()
        #frame_mapa.place(x=0, y=0)


######################
#Iniciar ventana     #
######################
frame_menu.mainloop()