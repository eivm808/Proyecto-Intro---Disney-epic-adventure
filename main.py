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

fondo_me = tk.Label(frame_menu, image=fondomenu_tk)
fondo_me.place(x=0, y=0)

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

fondo_av = tk.Label(frame_avatares, image=fondo_avatares_tk)
fondo_av.place(x=0, y=0)

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

###Fondo personajes###

frame_personajes = tk.Frame(root, width = 1280, height=720, bg="black")

ruta_fondo_personajes = "Assets\\Imagenes\\Fondos\\Fondo personajes.png"
fondo_personajes = Image.open(ruta_fondo_personajes)
fondo_personajes = fondo_personajes.resize((1280,720))
fondo_personajes_tk = ImageTk.PhotoImage(fondo_personajes)

fondo_pe = tk.Label(frame_personajes, image=fondo_personajes_tk)
fondo_pe.place(x=0, y=0)


###SELECCIONES DE BOTONES###

#Leer archivo de texto

def cargar_personajes():
     personajes = []
     archivo = open("data\\personajes.txt", "r") #open abre el archivo
     for linea in archivo:#recorre cada linea
          linea = linea.strip()
          datos = linea.split(",")#convierte en una lista
          personaje = {
               "nombre": datos[0],
               "HP": int(datos[1]),
               "ATK": int(datos[2]),#convierte el texto a int
               "DEF": int(datos[3]),

          }
          personajes.append(personaje)#agrega a la lista
     archivo.close()
     return personajes

lista_personajes = cargar_personajes()

#Funcion ver personajes, Boton SELECT

label_nombre_panel = tk.Label(frame_personajes, text="", font=("Courier New", 20), fg="green", bg="black")
label_nombre_panel.place(x = 190, y=290)

label_hp = tk.Label(frame_personajes, text="", font=("Courier New", 18), fg="green", bg="black")
label_hp.place(x=200, y=360)

label_atk = tk.Label(frame_personajes, text="", font=("Courier New", 18), fg="green", bg="black")
label_atk.place(x = 200, y=415)

label_def = tk.Label(frame_personajes, text="", font=("Courier New", 18), fg="green", bg="black")
label_def.place(x=200, y=470)

avatar_seleccionado = None
personaje_actual = None

def ver_personajes(nombre, hp, atk, defensa):
     global personaje_actual
     personaje_actual = {"nombre": nombre, "HP": hp, "ATK": atk, "DEF": defensa}
     label_nombre_panel.config(text=nombre)
     label_hp.config(text=f"HP: {hp}")
     label_atk.config(text=f"ATK: {atk}")
     label_def.config(text=f"DEF: {defensa}")

###Botones###

#Freddy

ruta_freddy = "Assets\\Imagenes\\Personajes\\Freddy.png"
foto_freddy = Image.open(ruta_freddy)
foto_freddy = foto_freddy.resize((100,100))
foto_freddy_tk = ImageTk.PhotoImage(foto_freddy)

btn_freddy = tk.Button(frame_personajes, image=foto_freddy_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[0]: ver_personajes(p["nombre"], p["HP"], p["ATK"], p["DEF"]))
btn_freddy.place(x=600,y=200)


#Withered bonnie

ruta_wbonnie = "Assets\\Imagenes\\Personajes\\W. Bonnie.png"
foto_wbonnie = Image.open(ruta_wbonnie)
foto_wbonnie = foto_wbonnie.resize((100,100))
foto_wbonnie_tk = ImageTk.PhotoImage(foto_wbonnie)

btn_wbonnie = tk.Button(frame_personajes, image=foto_wbonnie_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[1]: ver_personajes(p["nombre"], p["HP"], p["ATK"], p["DEF"]))
btn_wbonnie.place(x=720,y=200)

#Nightmare Fredbear

ruta_fredbear = "Assets\\Imagenes\\Personajes\\N. Fredbear.png"
foto_fredbear= Image.open(ruta_fredbear)
foto_fredbear = foto_fredbear.resize((100,100))
foto_fredbear_tk = ImageTk.PhotoImage(foto_fredbear)

btn_fredbear = tk.Button(frame_personajes, image=foto_fredbear_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[2]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_fredbear.place(x=840,y=200)

#Funtime Foxy

ruta_Ffoxy = "Assets\\Imagenes\\Personajes\\Funtime Foxy.png"
foto_Ffoxy = Image.open(ruta_Ffoxy)
foto_Ffoxy = foto_Ffoxy.resize((100,100))
foto_Ffoxy_tk = ImageTk.PhotoImage(foto_Ffoxy)

btn_Ffoxy = tk.Button(frame_personajes, image=foto_Ffoxy_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[3]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_Ffoxy.place(x=960,y=200)

#Scrap Baby

ruta_baby = "Assets\\Imagenes\\Personajes\\S. Baby.png"
foto_baby = Image.open(ruta_baby)
foto_baby = foto_baby.resize((100,100))
foto_baby_tk = ImageTk.PhotoImage(foto_baby)

btn_baby = tk.Button(frame_personajes, image=foto_baby_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[4]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_baby.place(x=1080,y=200)

#Bonnie

ruta_Bonnie = "Assets\\Imagenes\\Personajes\\Bonnie.png"
foto_Bonnie = Image.open(ruta_Bonnie)
foto_Bonnie = foto_Bonnie.resize((100,100))
foto_Bonnie_tk = ImageTk.PhotoImage(foto_Bonnie)

btn_Bonnie = tk.Button(frame_personajes, image=foto_Bonnie_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[5]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_Bonnie.place(x=600,y=350)

#Mangle

ruta_Mangle = "Assets\\Imagenes\\Personajes\\Mangle.png"
foto_Mangle = Image.open(ruta_Mangle)
foto_Mangle = foto_Mangle.resize((100,100))
foto_Mangle_tk = ImageTk.PhotoImage(foto_Mangle)

btn_Mangle = tk.Button(frame_personajes, image=foto_Mangle_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[6]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_Mangle.place(x=720,y=350)

#Nightmarionne

ruta_nightmarionne = "Assets\\Imagenes\\Personajes\\Nightmarionne.png"
foto_nightmarionne = Image.open(ruta_nightmarionne)
foto_nightmarionne = foto_nightmarionne.resize((100,100))
foto_nightmarionne_tk = ImageTk.PhotoImage(foto_nightmarionne)

btn_nightmarionne = tk.Button(frame_personajes, image=foto_nightmarionne_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[7]: ver_personajes(p["nombre"], p["HP"], p["ATK"],p["DEF"]))
btn_nightmarionne.place(x=840,y=350)


#Ennard

ruta_Ennard = "Assets\\Imagenes\\Personajes\\Ennard.png"
foto_Ennard = Image.open(ruta_Ennard)
foto_Ennard = foto_Ennard.resize((100,100))
foto_Ennard_tk = ImageTk.PhotoImage(foto_Ennard)

btn_Ennard = tk.Button(frame_personajes, image=foto_Ennard_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[8]: ver_personajes(p["nombre"], p["HP"], p["ATK"],p["DEF"]))
btn_Ennard.place(x=960,y=350)


#Puppet

ruta_Puppet = "Assets\\Imagenes\\Personajes\\Puppet.png"
foto_Puppet = Image.open(ruta_Puppet)
foto_Puppet = foto_Puppet.resize((100,100))
foto_Puppet_tk = ImageTk.PhotoImage(foto_Puppet)

btn_Puppet = tk.Button(frame_personajes, image=foto_Puppet_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[9]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_Puppet.place(x=1080,y=350)


#Foxy

ruta_foxy = "Assets\\Imagenes\\Personajes\\Foxy.png"
foto_foxy = Image.open(ruta_foxy)
foto_foxy = foto_foxy.resize((100,100))
foto_foxy_tk = ImageTk.PhotoImage(foto_foxy)

btn_foxy= tk.Button(frame_personajes, image=foto_foxy_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[10]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_foxy.place(x=600,y=500)


#Toy Chica

ruta_Tchica = "Assets\\Imagenes\\Personajes\\T. Chica.png"
foto_Tchica = Image.open(ruta_Tchica)
foto_Tchica = foto_Tchica.resize((100,100))
foto_Tchica_tk = ImageTk.PhotoImage(foto_Tchica)

btn_Tchica = tk.Button(frame_personajes, image=foto_Tchica_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[11]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_Tchica.place(x=720,y=500)


#Nightmare Chica

ruta_Nchica = "Assets\\Imagenes\\Personajes\\N. Chica.png"
foto_Nchica = Image.open(ruta_Nchica)
foto_Nchica = foto_Nchica.resize((100,100))
foto_Nchica_tk = ImageTk.PhotoImage(foto_Nchica)

btn_Nchica = tk.Button(frame_personajes, image=foto_Nchica_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[12]: ver_personajes(p["nombre"], p["HP"],p["ATK"],p["DEF"]))
btn_Nchica.place(x=840,y=500)


#Ballora

ruta_ballora = "Assets\\Imagenes\\Personajes\\Ballora.png"
foto_ballora = Image.open(ruta_ballora)
foto_ballora = foto_ballora.resize((100,100))
foto_ballora_tk = ImageTk.PhotoImage(foto_ballora)

btn_ballora = tk.Button(frame_personajes, image=foto_ballora_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[13]: ver_personajes(p["nombre"], p["HP"], p["ATK"], p["DEF"]))
btn_ballora.place(x=960,y=500)


#Lefty

ruta_lefty = "Assets\\Imagenes\\Personajes\\Lefty.png"
foto_lefty = Image.open(ruta_lefty)
foto_lefty = foto_lefty.resize((100,100))
foto_lefty_tk = ImageTk.PhotoImage(foto_lefty)

btn_lefty = tk.Button(frame_personajes, image=foto_lefty_tk, bd=0, relief="flat",
                       command=lambda p=lista_personajes[14]: ver_personajes(p["nombre"], p["HP"],p["ATK"], p["DEF"]))
btn_lefty.place(x=1080,y=500)




#############################################
#Mapa y seleccion de nivel                  #
#############################################

frame_mapa = tk.Frame(root, width = 1280, height=720, bg="black")

ruta_fondo_mapa = "Assets\\Imagenes\\Mapa\\mapa.png"
fondo_mapa = Image.open(ruta_fondo_mapa)
fondo_mapa = fondo_mapa.resize((1280,720))
fondo_mapa_tk = ImageTk.PhotoImage(fondo_mapa)

fondo_ma= tk.Label(frame_mapa, image=fondo_mapa_tk)
fondo_ma.place(x=0, y=0)

def ir_a_mapa():
        frame_avatares.forget()
        frame_mapa.place(x=0, y=0)


######################
#Iniciar ventana     #
######################
root.mainloop()