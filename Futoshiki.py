# Proyecto Programado 3
# Taller de Programación
# José Ricardo Cardona Quesada

# FUTOSHIKI

#-----------------------------------------------------------------------------------------------------------------------
# Librerías Utilizadas
import os
import pickle

# GUI
import tkinter as tk
from tkinter import messagebox
from datetime import *

#-----------------------------------------------------------------------------------------------------------------------
# Clases
class configuracion:

    # Puede ser Facil, Normal y Difícil
    dificultad = 'Facil'

    # Puede ser si, no y Timer
    reloj = 'Si'

    # Puede ser Derecha o Izquierda
    panel = 'Derecha'

    # Método para definir los datos de configuración:

    def __init__(self,nivel,clock,pan):

        # Se definen los datos del objeto con los nuevos datos de configuración
        self.dificultad = nivel
        self.reloj = clock
        self.panel = pan

    # Método para cambiar el nivel del objeto
    def cambiar_dificultad(self,nivel):
        self.dificultad = nivel

    # Método para cambiar la configuración en cuanto al reloj
    def cambiar_reloj(self,clock):
        self.reloj = clock

    # Método para cambiar la posición del panel de dígitos
    def cambiar_pos_panel(self,pan):
        self.panel = pan

    # Método para consultar los atributos de la configuración
    def consultar_atributos(self):
        return self.dificultad,self.reloj,self.panel

#-----------------------------------------------------------------------------------------------------------------------
# Variables,listas,etc..
futoshiki_config = configuracion

#-----------------------------------------------------------------------------------------------------------------------
# Funciones

#***********************************************************************************************************************
# Función 1 / Configuración
# Abre una ventana donde se pueden definir los datos de configuración para jugar fukoshiki



#-----------------------------------------------------------------------------------------------------------------------
# Programa Principal
# Se abre una ventana principal que tendrá las opciones del programa
# Se definen los datos de la ventana y sus botones
principal_futoshiki = tk.Tk()

principal_futoshiki.title('Super Futoshiki')
principal_futoshiki.geometry('750x750')

# Fondo
img1 = tk.PhotoImage(file = 'Fondo_futoshiki.png')
fondo_menu = tk.Label(principal_futoshiki, image = img1)
fondo_menu.place(x=0, y=-200, relwidth = 1)

# Botones y Labels
#Título
maintitle = tk.Label(principal_futoshiki, fg = 'black', relief = 'solid',  text ='FUTOSHIKI', font=('Times New Roman', 32), width = 15)
maintitle.place(x = 190, y = 50)

#Botones
jugar = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='JUGAR', font=('Times New Roman', 25))
jugar.place(x = 295, y = 160)

configurar = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='CONFIGURAR', font=('Times New Roman', 25))
configurar.place(x = 245, y = 280)

ayuda = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='AYUDA', font=('Times New Roman', 25))
ayuda.place(x = 295, y = 390)

Salir = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='SALIR', font=('Times New Roman', 25))
Salir.place(x = 305, y = 500)

principal_futoshiki.mainloop()