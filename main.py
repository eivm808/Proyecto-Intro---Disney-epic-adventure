# Proyecto 1 - Disney's Epic Adventure
# Introducción a la Programación - TEC




#---- Importacion Tkinter y pillow ----------------------------------


import tkinter as tk
from PIL import Image, ImageTk




#---- Ventana pricipal -----------------------------------------------------

root = tk.Tk()

frame_menu = tk.Frame(root, width=1280, height=720)
frame_menu.place(x=0, y=0)

root.title("Proyecto 01 Intro")
root.geometry("1280x720")



#---- Imagen Fondo ---------------------------------------------------------------------


ruta_fondomenu = "Assets\\Imagenes\\Fondos\\Menu freddy cabeza.png"
fondomenu = Image.open(ruta_fondomenu)
fondomenu = fondomenu.resize((1280,720))
fondomenu_tk = ImageTk.PhotoImage(fondomenu)

fondo_me = tk.Label(frame_menu, image=fondomenu_tk)
fondo_me.place(x=0, y=0)


#---- Titulo del juego ----------------------------------------------------------------------------------------------


titulo = tk.Label(frame_menu, text="Broken", font=('Times new roman',75), fg="#7d687d", bg="black")
titulo.place(x = 80, y = 100)
titulo2 = tk.Label(frame_menu, text="Circuits", font=('Times new roman',85), fg="#7d687d", bg="black")
titulo2.place(x = 80, y = 220)



#---- Boton ABOUT y entry de nombre -----------------------------------------------------------------------------------------------

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


#---- Ir a avatares --------------------------------------------------------------------------------------------------------------------------

###---- Cambio a frame de avatares y entry nombre ----###

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



#---- Seleccion de personajes ------------------------------------------------------------------------------------------------------------------------------------  

###FUNCIONES DE AVATARES###

def elegir_avatar(avatar_img):
    global avatar_seleccionado
    avatar_seleccionado = avatar_img
    frame_avatares.place_forget()
    frame_personajes.place(x=0, y=0)


###---- Botones imagenes de personajes ----###

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




#---- Frame y seleccion de personajes -------------------------------------------------------------------------------------------------------------------- 

###Fondo personajes###

frame_personajes = tk.Frame(root, width = 1280, height=720, bg="black")

ruta_fondo_personajes = "Assets\\Imagenes\\Fondos\\Fondo personajes.png"
fondo_personajes = Image.open(ruta_fondo_personajes)
fondo_personajes = fondo_personajes.resize((1280,720))
fondo_personajes_tk = ImageTk.PhotoImage(fondo_personajes)

fondo_pe = tk.Label(frame_personajes, image=fondo_personajes_tk)
fondo_pe.place(x=0, y=0)


###---- SELECCIONES DE BOTONES ----###

#Funcion Leer archivo de texto

def cargar_personajes(archivo, personajes=[]):
     linea = archivo.readline()
     if linea == "":
          archivo.close()
          return personajes
     linea = linea.strip()
     datos = linea.split(",")
     personaje = {
          "nombre": datos[0],
          "HP": int(datos[1]),
          "ATK": int(datos[2]),#convierte el texto a int
          "DEF": int(datos[3]),
     }
     personajes.append(personaje)#agrega a la lista
     archivo.close()
     return personajes

archivo = open("data\\personajes.txt", "r")
lista_personajes = cargar_personajes(archivo, [])

#Funcion ver personajes

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

     if personaje_actual in personajes_seleccionados:
          btnselect.config(text="DESELECT")
     else:
          btnselect.config(text="SELECT")

#---- Botones ------------------------------------------#

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

###---- Botones y label: select y continuar----###


#Funcion guardar personajes

personajes_seleccionados = []

def seleccionar_personajes():
     global personajes_seleccionados, personaje_actual

     if personaje_actual == None:
          return
     
     if personaje_actual in personajes_seleccionados:
          personajes_seleccionados.remove(personaje_actual)
          btnselect.config(text="SELECT")
          label_aviso.config(text=f"Seleccionados: {len(personajes_seleccionados)}/3")

     elif len(personajes_seleccionados) < 3:
          personajes_seleccionados.append(personaje_actual)
          btnselect.config(text="DESELECT")
          label_aviso.config(text=f"Seleccionados:{len(personajes_seleccionados)}/3")

     else:
          label_aviso.config(text="Ya tienes 3 personajes", fg='red')

     if len(personajes_seleccionados) == 3:
          btn_continuar.config(state="normal")
          
     else:
          btn_continuar.config(state="disabled")

#Boton select

btnselect = tk.Button(frame_personajes, text="SELECT", font=('Courier new', 16), bg='black', fg='green', relief='flat',
                      command=seleccionar_personajes)
btnselect.place(x=250, y=520)
btnselect.config(activebackground='black')
btnselect.config(activeforeground='green')

#---- Boton continuar ----------------------------------------------------------

def ir_a_mapa():
     frame_personajes.forget()
     frame_mapa.place(x=0, y=0)
    

btn_continuar = tk.Button(frame_personajes, text="CONTINUAR", font=("Courier new", 14), bg='black', fg='green',
                          state="disabled",command=ir_a_mapa)
btn_continuar.place(x=1050, y=650)

#---- Label -------------------------------------------------------------------

label_aviso = tk.Label(frame_personajes, text="Seleccionados: 0/3", font=("Courier New", 12), bg="black", fg="green")
label_aviso.place(x=250, y=550)

#############################################
#Mapa                                       #
#############################################

#---- Frame mapa ------------------------------------------

frame_mapa = tk.Frame(root, width = 1280, height=720, bg="black")

ruta_fondo_mapa = "Assets\\Imagenes\\Mapa\\mapa.png"
fondo_mapa = Image.open(ruta_fondo_mapa)
fondo_mapa = fondo_mapa.resize((1280,720))
fondo_mapa_tk = ImageTk.PhotoImage(fondo_mapa)

fondo_ma= tk.Label(frame_mapa, image=fondo_mapa_tk)
fondo_ma.place(x=0, y=0)

#############################################
#Seleccion de nivel                         #
#############################################

#---- Nivel 1 --------------------------------------------

### Funcion nivel 1 ###

def ir_a_n1():
     frame_mapa.forget()
     frame_n1.place(x=0, y=0)

### Boton nivel 1 ###

ruta_n01 = "Assets\\Imagenes\\Mapa\\cam01.jpeg"
foto_n01 = Image.open(ruta_n01)
foto_n01 = foto_n01.resize((100,80))
foto_n01_tk = ImageTk.PhotoImage(foto_n01)

btn_n1 = tk.Button(frame_mapa, image=foto_n01_tk, bd=0, relief="flat",
                   command=ir_a_n1)
btn_n1.place(x=950,y=540)

### Frame Nivel 1 ###

frame_n1 = tk.Frame(root, width = 1280, height=720, bg='black')




#---- Nivel 2 --------------------------------------------

### Funcion nivel 2 ###

def ir_a_n2():
     frame_mapa.forget()
     frame_n2.place(x=0, y=0)

### Boton nivel 2 ###

ruta_n02 = "Assets\\Imagenes\\Mapa\\cam02.jpeg"
foto_n02 = Image.open(ruta_n02)
foto_n02 = foto_n02.resize((100,80))
foto_n02_tk = ImageTk.PhotoImage(foto_n02)

btn_n02 = tk.Button(frame_mapa, image=foto_n02_tk, bd=0, relief="flat",
                    command=ir_a_n2)
btn_n02.place(x=950,y=200)

### Frame Nivel 2 ###

frame_n2 = tk.Frame(root, width = 1280, height=720, bg='black')

#---- Nivel 3 --------------------------------------------

### Funcion nivel 3 ###

def ir_a_n3():
     frame_mapa.forget()
     frame_n3.place(x=0, y=0)

### Boton nivel 3 ###

ruta_n03 = "Assets\\Imagenes\\Mapa\\cam03.jpeg"
foto_n03 = Image.open(ruta_n03)
foto_n03 = foto_n03.resize((100,80))
foto_n03_tk = ImageTk.PhotoImage(foto_n03)

btn_n03 = tk.Button(frame_mapa, image=foto_n03_tk, bd=0, relief="flat",
                    command=ir_a_n3)
btn_n03.place(x=700,y=240)

### Frame Nivel 3 ###

frame_n3 = tk.Frame(root, width = 1280, height=720, bg='black')


#---- Nivel 4 --------------------------------------------

### Funcion nivel 4 ###

def ir_a_n4():
     frame_mapa.forget()
     frame_n4.place(x=0, y=0)


### Boton nivel 4 ###

ruta_n04 = "Assets\\Imagenes\\Mapa\\cam04.jpeg"
foto_n04 = Image.open(ruta_n04)
foto_n04 = foto_n04.resize((100,80))
foto_n04_tk = ImageTk.PhotoImage(foto_n04)

btn_n04 = tk.Button(frame_mapa, image=foto_n04_tk, bd=0, relief="flat",
                    command=ir_a_n4)
btn_n04.place(x=400,y=185)

### Frame Nivel 4 ###

frame_n4 = tk.Frame(root, width = 1280, height=720, bg='black')



#---- Nivel 5 --------------------------------------------

### Funcion nivel 5 ###

def ir_a_n5():
     frame_mapa.forget()
     frame_n5.place(x=0, y=0)

### Boton nivel 5 ###

ruta_n05 = "Assets\\Imagenes\\Mapa\\cam05.jpeg"
foto_n05 = Image.open(ruta_n05)
foto_n05 = foto_n05.resize((100,80))
foto_n05_tk = ImageTk.PhotoImage(foto_n05)

btn_n05 = tk.Button(frame_mapa, image=foto_n05_tk, bd=0, relief="flat",
                    command=ir_a_n5)
btn_n05.place(x=500,y=500)


### Frame Nivel 5 ###

frame_n5 = tk.Frame(root, width = 1280, height=720, bg='black')

#############################################
#Logica del juego - Cada nivel              #
#############################################

#---- Logica ----------------------------------------------------------------

### Hollows ###

hollows = [
     {
          "nombre": "Hollow 1",
          "mundo": "Freddy's Dinner",
          "personajes":[
               {"nombre": "Chica", "HP": 100, "ATK": 18, "DEF": 12},
               {"nombre": "Toy Bonnie", "HP": 95, "ATK": 20, "DEF": 10},
               {"nombre": "Golden Freddy", "HP": 130, "ATK": 15, "DEF": 18},
          ]
     },
     {
         "nombre": "Hollow 2",
          "mundo": "Sister Location",
          "personajes":[
               {"nombre": "Minireenas", "HP": 105, "ATK": 24, "DEF": 10},
               {"nombre": "Funtime Freddy", "HP": 120, "ATK": 16, "DEF": 16},
               {"nombre": "Circus Baby", "HP": 110, "ATK": 22, "DEF": 14}
          ]
     },
     {
          "nombre": "Hollow 3",
          "mundo": "Pizzaplex",
          "personajes": [
               {"nombre": "Glamrock Freddy", "HP": 130, "ATK": 20, "DEF": 18},
               {"nombre": "Roxy", "HP": 110, "ATK": 26, "DEF": 12},
               {"nombre": "Montgomery", "HP": 140, "ATK": 14, "DEF": 22}
          ]
     },
     {
          "nombre": "Hollow 4",
          "mundo": "Fazbear Frights",
          "personajes": [
               {"nombre": "Springtrap", "HP": 140, "ATK": 24, "DEF": 16},
               {"nombre": "Scraptrap", "HP": 130, "ATK": 26, "DEF": 14},
               {"nombre": "Burntrap", "HP": 150, "ATK": 22, "DEF": 18}
          ]
     },
     {
          "nombre": "Hollow 5",
          "mundo": "The void",
          "personajes": [
               {"nombre": "Shadow Freddy", "HP": 160, "ATK": 28, "DEF": 20},
               {"nombre": "Shadow bonnie", "HP": 150, "ATK": 30, "DEF": 18},
               {"nombre": "Nightmare", "HP": 180, "ATK": 25, "DEF": 22}
          ]
     } 
]


###------------------------- Variables globales de batalla --------------------------###

hollow_actual = None
personaje_hollow_actual = None
personaje_jugador_actual = None
indice_hollow = 0
indice_jugador = 0
puntaje_jugador = 0
puntaje_hollow = 0

###--------------------------------- Frames --------------------------------------------------------###

#---- Frame para escoger personaje ------------------------------------------------------------------------------------------

frame_selector = tk.Frame(root, bg="black", bd=2, relief="solid")

label_selector = tk.Label(frame_selector, text="Escoge un personaje", font=("Courier new", 14), fg="green", bg="black")
label_selector.pack(pady=10)

#---- Frame de batalla -----------------------------------------------------------------------------------------------------------

frame_batalla = tk.Frame(root, width=1280, height=720, bg="black")

#---- Fondo batalla ------------------------------------------------------------------------------------------------------------------

fondo_batalla = tk.Label(frame_batalla)
fondo_batalla.place(x=0, y=0)


###---------------------------------- Labels ----------------------------------------###

#---- Imagen personaje del hollow --------------------------------

label_img_hollow = tk.Label(frame_batalla, bg="black")
label_img_hollow.place(x=800,y=200)

#---- Imagen personaje del jugador --------------------------------

label_img_jugador = tk.Label(frame_batalla, bg="black")
label_img_jugador.place(x=200,y=200)

#---- Label mensaje -------------------------------------------------

label_mensaje = tk.Label(frame_batalla, text="", font=("Courier new", 12), fg="white", bg="black")
label_mensaje.place(x=400, y=550)

#---- Label nombre y hp hollow -------------------------------------------------

label_nombre_hollow = tk.Label(frame_batalla, text="", font=("Courier new", 16), fg="green", bg="black")
label_nombre_hollow.place(x=800, y=50)

label_hp_hollow = tk.Label(frame_batalla, text="", font=("Courier new", 14), fg="green", bg="black")
label_hp_hollow.place(x=800, y=90)

#---- Label nombre y hp jugador -------------------------------------------------

label_nombre_jugador = tk.Label(frame_batalla, text="", font=("Courier new", 16), fg = "green", bg="black")
label_nombre_jugador.place(x=100, y=400)

label_hp_jugador = tk.Label(frame_batalla, text="", font=("Courier new", 14), fg="green", bg="black")
label_hp_jugador.place(x=100, y=440)

#---- Label puntaje -------------------------------------------------

label_puntaje = tk.Label(frame_batalla, text="Puntaje: 0", font=("Courier new", 12), fg="green", bg="black")
label_puntaje.place(x=100, y=600)



#---------------------------- Funciones --------------------------------------------------------------


#---- Funcion que agrega botones de personajes disponibles -----------------------------------------------------------------

def agregar_boton_personaje(indice):
     if indice > len(personajes_seleccionados): #caso base
          return
     
     p= personajes_seleccionados[indice]

     if p["HP_actual"] > 0: #muestra si no esta en KO
          tk.Button(frame_selector,
                    text=f"{p['nombre']} - HP: {p['HP_actual']}",
                    font=("Courier new", 12), fg="green", bg="black", relief="flat",
                    command=lambda per=p: seleccionar_en_batalla(per)).pack(pady=5)
          
          agregar_boton_personaje(indice + 1) #se llama a si misma

#---- Funcion que se ejecuta cuando el jugador apreta uno de los botones del selector -----------------------------------------------------------------

def seleccionar_en_batalla(personaje):
     global personaje_jugador_actual, indice_juagdor
     personaje_jugador_actual = personaje #guarda el personaje escogido como actual
     indice_jugador = personajes_seleccionados.index(personaje)#actualiza el indice  para saber en que posicion de la lista esta ese personaje
     frame_selector.place_forget()#cierra el selector
     label_mensaje.config(text=f"Cambiaste a {personaje['nombre']}!")#muestra mensaje diciendo a quien cambio
     actualizar_batalla #actualiza la pantalla con el nuevo personaje


#---- Funcion que limpia botones viejos del selector -----------------------------------------------------------------

def limpiar_botones(widgets, indice=0):#limpia los botones de los personajes para que no se acumulen
     if indice >= len(widgets):
          return
     if isinstance(widgets[indice], tk.Button):
          widgets[indice].destroy()
     limpiar_botones(widgets, indice + 1)

#---- Funcion que coordina las funciones para limpiar y crear nuevo botones -----------------------------------------------------------------

def mostrar_selector():
     limpiar_botones(frame_selector.winfo_children())
     agregar_boton_personaje(0)
     frame_selector.place(x=400, y=200)



### Funciones recursivas de batalla ###

#---- Copia el HP original a HP actual -------------------------------------------------------------------------------

def copiar_hp(personajes, indice=0):
     if indice >= len(personajes): #caso base cuando ya copio todos
          return
     personajes[indice]["HP_actual"] = personajes[indice]["HP"]
     copiar_hp(personajes, indice + 1)


#---- Busca el siguiente personaje que no este en KO del jugador ----------------------------------------------------

def siguiente_jugador(indice):
     if indice >= len(personajes_seleccionados): #caso base, cuando ya no hay mas personajes
          return None
     if personajes_seleccionados[indice]["HP_actual"] > 0: #si tiene vida lo retorn
          return indice
     return siguiente_jugador(indice + 1) #si esta en KO, busca el siguiente


#---- Busca el siguiente personaje que no este en KO del hollow ------------------------------------------------------

def siguiente_hollow(indice):
     if indice >= len(hollow_actual["personajes"]): #caso base cuando ya no hay mas personajes
          return None
     if hollow_actual["personajes"][indice]["HP_actual"] > 0:
          return indice
     return siguiente_hollow(indice + 1)

#---- Iniciar batalla -------------------------------------------------------------------------------------------------

def iniciar_batalla(hollow, ruta_fondo):
     global hollow_actual, personaje_hollow_actual, personaje_jugador_actual
     global indice_hollow, indice_jugador, puntaje_jugador, puntaje_hollow

     #Cambiar fondo segun nivel
     fondo_img = Image.open(ruta_fondo)
     fondo_img = fondo_img.resize((1280,720))
     fondo_img_tk = ImageTk.PhotoImage(fondo_img)
     fondo_batalla.config(image=fondo_img_tk)
     fondo_batalla.image = fondo_img_tk

     hollow_actual = hollow
     indice_hollow = 0
     indice_jugador = 0
     puntaje_hollow = 0
     puntaje_jugador = 0

     #---- Copiar HP ------------
     copiar_hp(hollow["personajes"])
     copiar_hp(personajes_seleccionados)

     personaje_hollow_actual = hollow["personajes"][0]
     personaje_jugador_actual = personajes_seleccionados[0]

     frame_mapa.place_forget()
     frame_nivel.place(x=0, y=0)

     actualizar_batalla()


#---- actualiza la pantalla de batalla --------------------------------------------------------------------------------

def actualizar_batalla():
     label_nombre_jugador.config(text=personaje_jugador_actual["nombre"])
     label_hp_jugador.config(text=f"HP: {personaje_jugador_actual['HP_actual']}")
     label_nombre_hollow.config(text=personaje_hollow_actual["nombre"])
     label_hp_hollow.config(text=f"HP: {personaje_hollow_actual['HP_actual']}")


     #actualizar imagen de hollow
     img_h = Image.open(personaje_hollow_actual["imagen"])
     img_h = img_h.resize((150, 150))
     img_h_tk = ImageTk.PhotoImage(img_h)
     label_img_hollow.config(image=img_h_tk)
     label_img_hollow.image = img_h_tk

     #actualizar imagen de jugador
     img_j = Image.open(personaje_jugador_actual["imagen"])
     img_j = img_j.resize((150, 150))
     img_j_tk = ImageTk.PhotoImage(img_j)
     label_img_jugador.config(image=img_j_tk)
     label_img_jugador.image = img_j_tk




#---- Logica de ataque ----------------------------------------------------------------------------------------------

def atacar():
     global personaje_hollow_actual, personaje_jugador_actual
     global indice_hollow, indice_jugador, puntaje_jugador
     
     #---- turno del jugador, calcula el daño ----
     daño_jugador = personaje_jugador_actual["ATK"] - personaje_hollow_actual["DEF"]
     if daño_jugador < 1:
          daño_jugador = 1
     personaje_hollow_actual["HP_actual"] -= daño_jugador
     label_mensaje.config(text="{personaje_jugador_actual['nombre']} hizo {daño_jugador} de daño!")

     #---- si el personaje del hollow perdio ----
     if personaje_hollow_actual["HP_actual"] <= 0:
          personaje_hollow_actual["HP_actual"] = 0
          puntaje_jugador += 1
          
          #---- personaje del hollow pasa a ser del jugador con hp restaurado ----
          personajes_seleccionados.append({
               "nombre": personaje_hollow_actual["nombre"],
               "HP": personaje_hollow_actual["HP"],
               "ATK": personaje_hollow_actual["ATK"],
               "DEF":personaje_hollow_actual["DEF"],
               "HP_actual": personaje_hollow_actual["HP"]
          })

          #---- Buscar siguiente personaje del hollow ----
          indice_hollow += 1
          nuevo_indice = siguiente_hollow(indice_hollow)

          if nuevo_indice is None: #---- jugador gana cuando hollow sin personajes
               label_mensaje.config(text="Ganaste! El hollow fue derrotado")
               btn_atacar.config(state="disabled")
               actualizar_batalla()
               return
          else:
               indice_hollow = nuevo_indice
               personaje_hollow_actual = hollow_actual["personajes"][indice_hollow]
               label_mensaje.config(text=f"{personaje_hollow_actual["nombre"]} entra a pelear!")

     
     #---- Turno del hollow: ataca de forma aleatoria ---------
     import random

     daño_hollow = personaje_hollow_actual["ATK"] - personaje_jugador_actual["DEF"]
     if daño_hollow < 1:
          daño_hollow = 1
     personaje_jugador_actual["HP_actual"] -= daño_hollow

     #---- Si el personaje del jugador perdio ----
     if personaje_jugador_actual["HP_actual"] <= 0:
          personaje_jugador_actual["HP_actual"] = 0

          #---- Busca el siguiente personaje del jugador
          indice_jugador += 1
          nuevo_indice = siguiente_jugador(indice_jugador)

          if nuevo_indice is None: #---- jugador sin personajes, hollow gano 
               label_mensaje.config(text="Perdiste, el hollow gano.")
               btn_atacar.config(state="disabled")
               actualizar_batalla()
               return
          else: 
               indice_jugador = nuevo_indice
               personaje_jugador_actual = personajes_seleccionados[indice_jugador]
               label_mensaje.config(text=f"{personaje_jugador_actual['nombre']} entra a pelear!")

     actualizar_batalla()

#---- Cambiar personaje --------------------------------------------------------------------------------------------------------

def cambiar_personaje():
     global personaje_jugador_actual, indice_jugador

     #Busca el siguiente personaje disponible
     nuevo_indice = siguiente_jugador(indice_jugador + 1)

     if nuevo_indice is None:
          label_mensaje.config(text="No hay mas personajes disponibles")
     else:
          indice_jugador = nuevo_indice
          personaje_jugador_actual = personajes_seleccionados[indice_jugador]
          label_mensaje.config(text=f"Cambiaste a {personaje_jugador_actual['nombre']}!")
          actualizar_batalla()
          


###---------------------------------- Botones ----------------------------------------###

#---- Boton atacar -------------------------------------------------

btn_atacar = tk.Button(frame_batalla, text="ATACAR", font=("Courier new", 14), bg="black", fg="green", relief="flat",
                       command=atacar)
btn_atacar.place(x=100, y=620)

#---- Boton cambiar de personaje -------------------------------------------------

btn_cambiar = tk.Button(frame_batalla, text="CAMBIAR", font=("Courier  new", 14), bg="black", fg="green", relief="flat",
                        command=mostrar_selector)
btn_cambiar.place(x=700, y=620)

#---- Boton volver a mapa -------------------------------------------------

btn_volver_mapa = tk.Button(frame_batalla, text="VOLVER", font=("Courier new", 14), bg="black", fg="green", relief="flat",
                            command=lambda: [frame_batalla.place_forget(), frame_mapa.place(x=0, y=0)])
btn_volver_mapa.place(x=50, y=650)

      





######################
#Iniciar ventana     #
######################
root.mainloop()