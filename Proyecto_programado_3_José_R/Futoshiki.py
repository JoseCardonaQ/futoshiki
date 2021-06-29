# Proyecto Programado 3
# Taller de Programación
# José Ricardo Cardona Quesada

# FUTOSHIKI
print('hola Usuario')
#-----------------------------------------------------------------------------------------------------------------------
# Librerías Utilizadas
import os
import pickle

# GUI
import time
import tkinter as tk
from tkinter import messagebox
from datetime import *
import random

# Listas Importantes

# Tiene 3 listas, una por cada dificultad
# Cada jugador por dificultad será una tupla con el nombre y el tiempo
tp10 = open('futoshiki2021top10.dat','rb')
top_10 = pickle.load(tp10)

tp10.close()

# Partida Actual (Realmente es la partida guardada)
# Contiene una lista con los valores de todos los tiles, otra lista con las posiciones de aquellos que son fijos y la dificultad
# Se importa y se guarda en un DAT

partida_actual = []

# Partidas
# Se importa de un DAT
partidas = papapa = open('futoshiki2021partidas.dat','rb')
partidas = pickle.load(partidas)

# Contiene 3 partidas por dificultad, cada partida se representa con una tupla
partidas_faciles = partidas[0]

partidas_regulares = partidas[1]

partidas_dificiles = partidas[2]

#-----------------------------------------------------------------------------------------------------------------------
# Programa Principal

# Se abre una ventana principal que tendrá las opciones del programa
principal_futoshiki = tk.Tk()

# Variables y otros elementos importantes
# Datos de configuración (Pueden modificarse con la función configuración)

# Se van a importar del documento de configuración

configuracion = open('futoshiki2021configuración.dat','rb')
config = pickle.load(configuracion)

# La Dificultad
# Tiene 3 posibilidades: Facil, Intermedio, Dificil
# Comienza como Fácil la primera vez que se corra el programa
dificultad = tk.StringVar()
dificultad.set(config[0])

# El Reloj
# Puede ser Si, No o Timer
# Comienza como Si la primera vez que se corra el programa
reloj = tk.StringVar()
reloj.set(config[1])

# La posición en la ventana
# Puede ser Derecha o Izquierda
# La primera vez comienza como derecha
position = tk.StringVar()
position.set(config[2])

# Valores para el timer
# Solo se van a utilizar cuando el reloj sea timer
horas_timer = tk.IntVar()
horas_timer.set(config[3])

# A diferencia de el resto esta  variable comienza como 30
minutos_timer = tk.IntVar()
minutos_timer.set(config[4])

segundos_timer = tk.IntVar()
segundos_timer.set(config[5])

configuracion.close()

# Funciones
#***********************************************************************************************************************
# Función 1 / Configuración
# Abre una ventana donde se pueden definir los datos de configuración para jugar fukoshiki
# Esta ventana dependerá de la ventana principal y tendrá opciones limitadas para cada configuración

def configuracion():

    # Función anidada 1
    # Cuando este marcada la opción si o no en el reloj esta función se ejecuta para que no se pueda configurar el timer
    def deshabilitar_timer():
        hrs_tim.config(state='readonly')
        mins_tim.config(state = 'readonly')
        secs_tim.config(state='readonly')

    # Si se marca la opción timer se habilita el timer, para esto existe la función siguiente
    def habilitar_timer():
        hrs_tim.config(state= 'normal')
        mins_tim.config(state= 'normal')
        secs_tim.config(state= 'normal')

    # Las funciones para revisar y asignar un valor a las entradas del timer
    def verificar_horas(*args):
        valor = hrs_tim.get()

        # Se intenta reconocer las horas como un entero
        try:
            valor = int(valor)

            # Se revisa si es mayor o igual que 0
            if valor >= 0:

                # Si es válido se cambian para el timer
                horas_timer.set(valor)

            # Si no es válido
            else:
                hrs_tim.delete(0, 'end')
                hrs_tim.insert(0, horas_timer.get())
                messagebox.showinfo('Valor Inválido','El valor para las horas del timer debe ser >= 0',master =configuracion)

        # Si no se puede tomar como entero
        except:
            hrs_tim.delete(0,'end')
            hrs_tim.insert(0, horas_timer.get())
            messagebox.showinfo('Valor Inválido', 'El valor para las horas del timer debe ser un número entero >= 0',
                                   master=configuracion)

    def verificar_minutos(*args):
        valor = mins_tim.get()

        # Se intenta reconocer como un entero
        try:
            valor = int(valor)

            # Se revisa si esta entre 0 y 59
            if valor >= 0 and valor < 60:

                # Si es válido se cambian los minutos para el timer
                minutos_timer.set(valor)

            # Si no es válido
            else:
                mins_tim.delete(0, 'end')
                mins_tim.insert(0, minutos_timer.get())
                messagebox.showinfo('Valor Inválido', 'El valor para los minutos del timer debe estar entre 0 y 60',
                                       master=configuracion)

        # Si no se puede tomar como entero
        except:
            mins_tim.delete(0, 'end')
            mins_tim.insert(0, minutos_timer.get())
            messagebox.showinfo('Valor Inválido', 'El valor para los minutos del timer debe ser un entero entre 0 y 60',
                                   master=configuracion)

    def verificar_segundos(*args):
        valor = secs_tim.get()

        # Se intenta reconocer como un entero
        try:
            valor = int(valor)

            # Se revisa si esta entre 0 y 59
            if valor >= 0 and valor < 60:

                # Si es válido se cambian los minutos para el timer
                segundos_timer.set(valor)

            # Si no es válido
            else:
                secs_tim.delete(0, 'end')
                secs_tim.insert(0, segundos_timer.get())
                messagebox.showinfo('Valor Inválido', 'El valor para los segundos del timer debe estar entre 0 y 60',
                                       master=configuracion)

        # Si no se puede tomar como entero
        except:
            secs_tim.delete(0, 'end')
            secs_tim.insert(0, segundos_timer.get())
            messagebox.showinfo('Valor Inválido', 'El valor para los segundos del timer debe ser un entero entre 0 y 60',
                                   master=configuracion)

    configuracion = tk.Toplevel()
    configuracion.geometry('750x750')
    configuracion.title('Configuración del Juego')

    titulo = tk.Label(configuracion, text='Configuración', font=('Times New Roman', 18))
    titulo.place(x=10, y=5)

    # Para cambiar las dificultades
    dif = tk.Label(configuracion,fg = 'dark blue',  text='Dificultad:', font=('Times New Roman', 17))
    dif.place(x=10, y=50)

    # Botones para las posibles dificultades

    dificultad1 = tk.Radiobutton(configuracion,text = 'Fácil',font=('Times New Roman', 15) , variable =  dificultad, value = 'Facil')
    dificultad1.place(x = 10, y = 100)

    dificultad2 = tk.Radiobutton(configuracion,text = 'Intermedio',font=('Times New Roman', 15), variable =  dificultad, value = 'Intermedio')
    dificultad2.place(x=10, y=150)

    dificultad3 = tk.Radiobutton(configuracion,text = 'Dificil',font=('Times New Roman', 15), variable =  dificultad, value = 'Dificil')
    dificultad3.place(x=10, y=200)

    # Para cambiar la configuración del reloj
    con = tk.Label(configuracion,fg = 'dark blue',  text='Reloj:', font=('Times New Roman', 17))
    con.place(x=10, y=250)

    # Botones para las posibilidades
    s = tk.Radiobutton(configuracion, text='Si', font=('Times New Roman', 15), variable= reloj,
                                 value='Si',command = deshabilitar_timer)
    s.place(x=10, y=300)

    n = tk.Radiobutton(configuracion, text='No', font=('Times New Roman', 15), variable= reloj,
                                 value='No',command = deshabilitar_timer)
    n.place(x=10, y=350)

    timer = tk.Radiobutton(configuracion, text='Timer', font=('Times New Roman', 15), variable= reloj,
                                 value='Timer', command = habilitar_timer)
    timer.place(x=10, y=400)

    # La configuración también tendrá la opción de configurar un timer en caso de que se marque la opción timer, para esto habrán 3 entradas

    t = tk.Label(configuracion, text='TIMER', font=('Times New Roman', 18))
    t.place(x=330, y= 270)

    # Cada uno de estos puede cambiar los valores posibles para el timer al presionar enter

    hrs_tim = tk.Entry(configuracion,font=('Times New Roman', 18), width = 4)
    hrs_tim.insert(0,horas_timer.get())
    hrs_tim.place(x = 290, y = 320,height= 50)

    mins_tim = tk.Entry(configuracion, font=('Times New Roman', 18), width = 4)
    mins_tim.insert(0, minutos_timer.get())
    mins_tim.place(x=345, y=320,height= 50)

    secs_tim = tk.Entry(configuracion,font=('Times New Roman', 18), width = 4)
    secs_tim.insert(0,segundos_timer.get())
    secs_tim.place(x=400, y=320, height= 50)

    # Para revisar y asignar valores a los entries
    hrs_tim.bind('<Return>', verificar_horas)
    mins_tim.bind('<Return>', verificar_minutos)
    secs_tim.bind('<Return>', verificar_segundos)

    # Si el reloj no esta en timer no se podrán modificar
    if reloj.get() != 'Timer':
        hrs_tim.config(state='readonly')
        mins_tim.config(state='readonly')
        secs_tim.config(state='readonly')

    # Para cambiar la configuración del panel de dígitos

    con = tk.Label(configuracion, fg='dark blue', text='Posición en la ventana del panel de dígitos:', font=('Times New Roman', 17))
    con.place(x=10, y=450)

    # Botones
    pos = tk.Radiobutton(configuracion, text='Derecha', font=('Times New Roman', 15), variable= position,
                           value='Derecha')
    pos.place(x=10, y=500)

    pos = tk.Radiobutton(configuracion, text='Izquierda', font=('Times New Roman', 15), variable= position,
                         value='Izquierda')
    pos.place(x=10, y=550)

    # También habrá un botón para salir de la configuración
    out = tk.Button(configuracion, fg = 'white', bg = 'red',  relief = 'solid',  text ='SALIR', font=('Times New Roman', 25), command = configuracion.destroy)
    out.place(x = 295, y =600)

# Función principal 2 (Jugar)
# Esta función abre una ventana donde se podrá jugar un mapa seleccionado de futoshiki
# La forma en que se verá la ventana dependerá siempre de la configuración

def jugar_futoshiki(cargado):

    # Según el nivel de dificultad se importará aleatoriamente un mapa de futoshiki para completar
    # Para seleccionar aleatoriamente se va a utilizar el método randint para seleccionar un índice aleatorio de la lista de mapas de esa dificultad

    if cargado == []:

        if dificultad.get() == 'Facil':
            mapa = partidas_faciles[random.randint(0, 2)]

        elif dificultad.get() == 'Intermedio':
            mapa = partidas_regulares[random.randint(0, 2)]

        else:
            mapa = partidas_dificiles[random.randint(0, 2)]

    else:
        mapa = cargado[1]

    if cargado != []:
        dificultad.set(cargado[2][0])

    #-------------------------------------------------------------------------------------------------------------------
    futoshiki = tk.Toplevel()

    # Funciones de la ventana

    # Función para guardar juego
    def guardar_juego():

        # Se importa el archivo
        guardar_j = open('futoshiki2021juegoactual.dat','wb')

        # Se forma una lista con los valores actuales de cada tile
        valores = []

        for fila in range(len(tiles)):
            f = []
            for columna in range(len(tiles[fila])):

                f.append((tiles[fila][columna]['text'] , fila,columna))

            valores.append(f)

        # Se crea una lista con los datos necesarios
        datos_g = [lista_jugadas,mapa,(dificultad.get(),nombre_jugador.get(),(horas.get(),minutos.get(),segundos.get()))
                   ,valores]

        # Se guarda la lista en el archivo
        pickle.dump(datos_g,guardar_j)
        guardar_j.close()

        # Se envía un mensaje
        messagebox.showinfo('Guardado Exitoso!', 'La partida fue guardada exitosamente',master= futoshiki)

    # Función para cargar el juego
    def cargar_juego():

        # Se abre el archivo de juego actual
        juego_c = open('futoshiki2021juegoactual.dat','rb')
        juego_cargado = pickle.load(juego_c)

        # Se destruye la ventana actual
        futoshiki.destroy()

        # Se abre una ventana nueva con el mapa nuevo y los datos obtenidos
        jugar_futoshiki(juego_cargado)

    # Función para el top10 (Abre una ventana nueva)
    def abrir_top():

        bruh = tk.Toplevel(futoshiki)
        bruh.geometry('900x1000')
        bruh.title('Top 10')

        # Labels fijos
        t = tk.Label(bruh, text = 'TOP 10', font = ('Times New Roman', 24))
        t.place(x = 380, y = 10)

        f = tk.Label(bruh, text = 'Fácil', font = ('Times New Roman', 20))
        f.place(x = 100, y = 70)

        f = tk.Label(bruh, text='Intermedio', font=('Times New Roman', 20))
        f.place(x=370, y=70)

        f = tk.Label(bruh, text='Difícil', font=('Times New Roman', 20))
        f.place(x=700, y=70)

        # Para los nombres, records y posición de los demás
        # Facil
        # Si esta vacío
        if top_10[0] == []:

            v = tk.Label(bruh, text='No hay jugadores registrados', font=('Times New Roman', 14))
            v.place(x=40, y= 130)

        # Si no esta vacío
        else:

            j = tk.Label(bruh, text='Jugador', font=('Times New Roman', 14))
            j.place(x=30, y=130)

            rre = tk.Label(bruh, text='Tiempo', font=('Times New Roman', 14))
            rre.place(x=180, y=130)

            y = 180

            for jugador in range(1,len(top_10[0])+1):

                jogador = top_10[0][jugador-1][0]
                time = top_10[0][jugador-1][1]

                label = tk.Label(bruh, text= str(jugador) + '. ' + jogador, font=('Times New Roman', 14))
                label.place(x=30, y = y)

                tiempo = tk.Label(bruh, text= time , font=('Times New Roman', 14))
                tiempo.place(x=180, y = y)

                y += 50

        # Intermedio
        if top_10[1] == []:

            v = tk.Label(bruh, text='No hay jugadores registrados', font=('Times New Roman', 14))
            v.place(x=310, y=130)

        # Si no esta vacío
        else:

            j = tk.Label(bruh, text='Jugador', font=('Times New Roman', 14))
            j.place(x=320, y=130)

            rre = tk.Label(bruh, text='Tiempo', font=('Times New Roman', 14))
            rre.place(x=450, y=130)

            y = 180

            for jugador in range(1, len(top_10[1]) + 1):
                jogador = top_10[1][jugador - 1][0]
                time = top_10[1][jugador - 1][1]

                label = tk.Label(bruh, text=str(jugador) + '. ' + jogador, font=('Times New Roman', 14))
                label.place(x=320, y=y)

                tiempo = tk.Label(bruh, text=time, font=('Times New Roman', 14))
                tiempo.place(x=450, y=y)

                y += 50

        # Difícil
        if top_10[2] == []:

            v = tk.Label(bruh, text='No hay jugadores registrados', font=('Times New Roman', 14))
            v.place(x=640, y=130)

        # Si no esta vacío
        else:

            j = tk.Label(bruh, text='Jugador', font=('Times New Roman', 14))
            j.place(x=630, y=130)

            rre = tk.Label(bruh, text='Tiempo', font=('Times New Roman', 14))
            rre.place(x=780, y=130)

            y = 180

            for jugador in range(1, len(top_10[2]) + 1):
                jogador = top_10[2][jugador - 1][0]
                time = top_10[2][jugador - 1][1]

                label = tk.Label(bruh, text=str(jugador) + '. ' + jogador, font=('Times New Roman', 14))
                label.place(x=630, y=y)

                tiempo = tk.Label(bruh, text=time, font=('Times New Roman', 14))
                tiempo.place(x=780, y=y)

                y += 45

    # Función para el relloj / timer
    def reloj_timer():

        if terminar_reloj.get() == 'No':

            if reloj.get() == 'Si':
                if int(segundos.get()) + 1 < 60:
                    segundos.set(int(segundos.get()) + 1)

                    horas_display.config(text=horas.get())
                    minutos_display.config(text=minutos.get())
                    segundos_display.config(text=segundos.get())

                else:
                    segundos.set(0)
                    if int(minutos.get()) + 1 < 60:
                        minutos.set(int(minutos.get()) + 1)

                        horas_display.config(text = horas.get())
                        minutos_display.config(text = minutos.get())
                        segundos_display.config(text = segundos.get())

                    else:
                        minutos.set(0)
                        horas.set(int(horas.get()) + 1)

                        horas_display.config(text = horas.get())
                        minutos_display.config(text = minutos.get())
                        segundos_display.config(text = segundos.get())

                futoshiki.after(1000, reloj_timer)

            elif reloj.get() == 'Timer':

                if int(segundos.get()) - 1 < 0:

                    if int(minutos.get()) - 1 < 0:

                        if int(horas.get()) - 1 < 0:

                            horas_display.config(text = 0)
                            minutos_display.config(text = 0)
                            segundos_display.config(text = 0)

                            # Se actualizan los valores

                            # Se deshabilita la ventana
                            futoshiki.grab_set()

                            terminar_reloj.set('Si')

                            # Se envía un mensaje para preguntar si se desea continuar
                            x = messagebox.askquestion('Tiempo terminado!',
                                                       'Atención: Se acabo el tiempo \n ¿Desea Continuar?',master= futoshiki)

                            if x == 'yes':
                                # Se pasa el reloj de timer a reloj normal
                                reloj.set('Si')
                                terminar_reloj.set('No')

                                horas.set(int(horas_timer.get()))
                                minutos.set(int(minutos_timer.get()))
                                segundos.set(int(segundos_timer.get()))

                                # Se rehabilita la ventana
                                futoshiki.grab_release()

                            # Si no
                            else:
                                # Se cierra la ventana
                                futoshiki.destroy()

                                # Se abre una nueva
                                jugar_futoshiki([])

                        else:
                            horas.set(int(horas.get() - 1))
                            minutos.set(59)
                            segundos.set(59)

                            horas_display.config(text=horas.get())
                            minutos_display.config(text=minutos.get())
                            segundos_display.config(text=segundos.get())

                    else:
                        minutos.set(int(minutos.get()) - 1)
                        segundos.set(59)

                        horas_display.config(text = horas.get())
                        minutos_display.config(text = minutos.get())
                        segundos_display.config(text = segundos.get())

                else:
                    segundos.set(int(segundos.get()) - 1)

                    horas_display.config(text=horas.get())
                    minutos_display.config(text=minutos.get())
                    segundos_display.config(text=segundos.get())

                futoshiki.after(1000, reloj_timer)

            else:
                pass

        else:
            pass

    # Función para iniciar el juego
    # Verifica que haya un nombre ingresado
    # Al insertar un nombre válido habilita el botón iniciar juego
    # Debe buscar que no este en la lista de Top 10 de cualquier nivel

    def iniciar_juego(*args):

        n = playername.get()

        # Se verifica si esta vacío
        if n != '':

            # Se verifica si tiene entre 1 y 20 caracteres
            if len(n) <= 20:

                # Se van a revisar todas las listas de top10 para verificar que el nombre no exista todavía en un top10
                existe = False

                for nivel in top_10:

                    for jug in nivel:

                        if jug[0] == n:
                            existe = True
                            break

                if existe == True:
                    messagebox.showerror("Nombre Inválido",
                                         'El nombre ingresado ya existe dentro del top10 de algún nivel',master= futoshiki)

                else:

                    # Se le asigna ese nombre a la variable de nombre
                    nombre_jugador.set(n)

                    # Se le asigna a la variable de tiempo de inicio el tiempo actual
                    global tiempo_inicial
                    tiempo_inicial = datetime.now()

                    # Se habilitan todos los botones
                    for fila in tiles:
                        for boton in fila:
                            boton.config(state='normal')

                    # Se deshabilitan aquellos quue son fijos
                    # Finalmente para los números fijos
                    for restriccion in mapa:
                        if restriccion[0].isdigit():
                            tiles[restriccion[1]][restriccion[2]].config(state='disabled')

                    # Habilita los botones de dígitos
                    d_1.config(state='normal')
                    d_2.config(state='normal')
                    d_3.config(state='normal')
                    d_4.config(state='normal')
                    d_5.config(state='normal')

                    # Se deshabilita a el botón para iniciar juego
                    startgame.config(state='disabled')
                    # Se desabilita el entry
                    playername.config(state='readonly')
                    # Se deshabilita cargar juego
                    cj.config(state='disabled')

                    # Corre la función para el reloj / timer
                    reloj_timer()

                    # Habilita el resto de botones de la ventana
                    erase.config(state='normal')
                    erase_game.config(state='normal')
                    finish.config(state='normal')
                    gj.config(state='normal')

            else:
                messagebox.showerror("Nombre Inválido", 'El nombre ingresado debe tener una longitud máxima de 20 caracteres',master= futoshiki)
        else:
            messagebox.showerror("No se Inserto Nombre",'Para iniciar el juego inserte un nombre de entre 1 y 20 caracteres',master= futoshiki)


    # Función 2
    # Esta función determinará lo que sucede cuando se clickea cualquiera de los botones activos para el futoshiki

    # Falta que guarde en LIFO
    def activar_tile(boton):

        # Funciones para regresar errores
        def regresar_error_horizontal(b):
            messagebox.showinfo('Ya existe', 'La Jugada no es válida porque el elemento ya existe en la fila',master= futoshiki)
            b.config(bg = 'white')

        def regresar_error_vertical(b):
            messagebox.showinfo('Ya existe', 'La Jugada no es válida porque el elemento ya existe en la columna',master= futoshiki)
            b.config(bg='white')

        def regresar_invalidez_horizontal(b,tipo, lado):
            if tipo == '>' and lado == 'D':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de mayor',master= futoshiki)
                b.config(bg='white')

            elif tipo == ">" and lado == 'I':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de menor',master= futoshiki)
                b.config(bg='white')

            elif tipo == '<' and lado == 'D':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de menor',master= futoshiki)
                b.config(bg='white')

            else:
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de mayor',master= futoshiki)
                b.config(bg='white')

        def regresar_invalidez_vertical(b,tipo, lado):
            if tipo == 'V' and lado == 'S':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de mayor',master= futoshiki)
                b.config(bg='white')

            elif tipo == 'V' and lado == 'I':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de menor',master= futoshiki)
                b.config(bg='white')

            elif tipo == '˄' and lado == 'S':
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de mayor',master= futoshiki)
                b.config(bg='white')

            else:
                messagebox.showinfo('Jugada Inválida', 'No cumple con la restricción de menor',master= futoshiki)
                b.config(bg='white')

        #---------------------------------------------------------------------------------------------------------------

        valor = numero_actual.get()

        #   Si no se ha insertado ningún valor dará un error
        if valor == '':
            messagebox.showinfo('Falta Valor!', 'Para realizar esto seleccione un dígito que insertar primero',master= futoshiki)

        # Si ya se selecciono el valor
        else:

            valor = int(valor)

            # Se van a encontrar la fila y columna a la que pertenece el botón
            fila = 0
            columna = 0

            for n_fila in range(len(tiles)):
                line = tiles[n_fila]

                for n_columna in range(len(line)):
                    button = line[n_columna]

                    # Cuando se encuentre el botón se guardan sus índices
                    if button == boton:
                        fila = n_fila
                        columna = n_columna

                        break

            # Tras encontrar sus índices se verifica se cumplen las restricciones a su alrededor
            # Primero se verifica que no exista horizontalmente, para esto se usa el índice de fila obtenido

            ya_existe_hor = False

            # Por cada valor en esa fila
            for t in tiles[fila]:

                if t == boton:
                    pass

                else:
                    # Si esta vacía no se compara
                    if t['text'] == '':
                        pass

                    else:
                        # Se obtiene el valor a comparar
                        comparar = int(t['text'])

                        # Se verifica que su valor no sea igual al que se quiere insertar será inválido
                        if comparar == valor:
                            ya_existe_hor = True
                            break

            # Se verifica si se marco como que ya  existía
            if ya_existe_hor == True:
                boton.config(bg = 'red')
                regresar_error_horizontal(boton)

            # Si no existe horizontal se busca de forma vertical
            else:

                ya_existe_ver = False

                for f in tiles:
                    tile = f[columna]

                    if tile == boton:
                        pass

                    else:
                        if tile['text'] == '':
                            pass

                        else:
                            # Se obtiene el valor a comparar
                            comparar = int(tile['text'])

                            if comparar == valor:
                                ya_existe_ver = True
                                break

                if ya_existe_ver == True:
                    boton.config(bg='red')
                    regresar_error_vertical(boton)
                # Si tampoco se repite verticalmente se va a verificar si cumple con las restricciones, si las tiene
                else:

                    # Para las restricciones horizontales
                    # Para esto se busca según la lista restricciones horizontales

                    # Variable para ver si cumple con su relacion horizontal
                    cumple_horizontal = True
                    relacion_no_cumplida = ''
                    lado = 'D'

                    # Si la columna es 0 solo se revisa a la derecha
                    if columna == 0:

                        # Se obtiene el símbolo para esa fila y esa columna
                        tipo_r = restricciones_horizontales[fila][columna]['text']

                        # Si el cuadro a su derecha no esta vacío

                        if tiles[fila][columna + 1]['text'] == '':
                            pass

                        else:

                            # Si hay una relación de mayor que horizontal
                            if tipo_r == '>':

                                # Si cumple con esa restricción

                                if valor > int(tiles[fila][columna + 1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = tipo_r
                                    cumple_horizontal = False
                                    lado = 'D'

                            elif tipo_r == '<':

                                # Si cumple con esa restricción

                                if valor < int(tiles[fila][columna + 1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = tipo_r
                                    cumple_horizontal = False
                                    lado = 'D'

                            # Si no hay restricción se pasa
                            else:
                                pass

                    # Si es la última columna solo se revisa a la izquierda
                    elif columna == 4:

                        tipo_r = restricciones_horizontales[fila][columna-1]['text']
                        # Si el cuadro a su izquierda no esta vacío

                        if tiles[fila][columna -1]['text'] == '':
                            pass

                        else:

                            # Si hay una relación de mayor que horizontal
                            if tipo_r == '>':

                                # Si cumple con esa restricción
                                if valor < int(tiles[fila][columna -1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = tipo_r
                                    cumple_horizontal = False
                                    lado = 'I'

                            elif tipo_r == '<':

                                # Si cumple con esa restricción
                                if valor > int(tiles[fila][columna -1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = tipo_r
                                    cumple_horizontal = False
                                    lado = 'I'

                            # Si no hay restricción se pasa
                            else:
                                pass

                    # Si no esta ni en la primera ni en la última columna
                    # Se deben revisar ambos lados
                    else:
                        restric_izquierda = restricciones_horizontales[fila][columna -1]['text']
                        restric_derecha = restricciones_horizontales[fila][columna]['text']

                        # Primero se revisa el lado izquierdo
                        # Si el cuadro a su izquierda no esta vacío

                        if tiles[fila][columna -1]['text'] == '':
                            pass

                        else:

                            # Si hay una relación de mayor que horizontal
                            if restric_izquierda == '>':

                                # Si cumple con esa restricción
                                if valor < int(tiles[fila][columna -1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = restric_izquierda
                                    cumple_horizontal = False
                                    lado = 'I'

                            elif restric_izquierda == '<':

                                # Si cumple con esa restricción
                                if valor > int(tiles[fila][columna -1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = restric_izquierda
                                    cumple_horizontal = False
                                    lado = 'I'

                            # Si no hay restricción se pasa
                            else:
                                pass

                        # Luego se revisa el lado derecho
                        # Si el cuadro a su derecha no esta vacío
                        if tiles[fila][columna + 1]['text'] == '':
                            pass

                        else:

                            # Si hay una relación de mayor que horizontal
                            if restric_derecha == '>':

                                # Si cumple con esa restricción
                                if valor > int(tiles[fila][columna + 1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = restric_derecha
                                    cumple_horizontal = False
                                    lado = 'D'

                            elif restric_derecha == '<':

                                # Si cumple con esa restricción
                                if valor < int(tiles[fila][columna + 1]['text']):
                                    pass

                                else:
                                    relacion_no_cumplida = restric_derecha
                                    cumple_horizontal = False
                                    lado = 'D'

                            # Si no hay restricción se pasa
                            else:
                                pass

                    # Tras verificar las restricciones horizontales se decide si enviar un mensaje de error
                    # Si no se cumple
                    if cumple_horizontal == False:
                        boton.config(bg='red')
                        regresar_invalidez_horizontal(boton,relacion_no_cumplida,lado)

                    # Si cumple con las validaciones horizontales
                    # Se van a verificar las validaciones verticales
                    else:
                        # Variables para la revisión
                        cumple_vertical = True
                        relacion_no_cumplida_ver = ''
                        lado_v = 'S'

                        # Si la fila es 0 solo se revisa hacia abajo
                        if fila == 0:

                            # Se obtiene el símbolo para esa fila y esa columna
                            tipo_r_v = restricciones_verticales[fila][columna]['text']

                            # Si el cuadro a su derecha no esta vacío
                            if tiles[fila + 1][columna]['text'] == '':
                                pass

                            else:

                                # Si hay una relación de mayor que horizontal
                                if tipo_r_v == 'V':

                                    # Si cumple con esa restricción
                                    if valor > int(tiles[fila + 1][columna]['text']):
                                       pass

                                    else:
                                        relacion_no_cumplida_ver = tipo_r_v
                                        cumple_vertical = False
                                        lado_v = 'S'

                                elif tipo_r_v == '˄':
                                    # Si cumple con esa restricción

                                    if valor < int(tiles[fila + 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = tipo_r_v
                                        cumple_vertical = False
                                        lado_v = 'S'

                                # Si no hay restricción se pasa
                                else:
                                    pass

                        # Si la fila es 4 solo se revisa hacia arriba
                        elif fila == 4:

                            tipo_r_v = restricciones_verticales[fila - 1][columna]['text']

                            # Si el cuadro arriba esta vacío
                            if tiles[fila-1][columna]['text'] == '':
                                pass

                            else:

                                # Si hay una relación de mayor que horizontal
                                if tipo_r_v == 'V':

                                    # Si cumple con esa restricción
                                    if valor < int(tiles[fila - 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = tipo_r_v
                                        cumple_vertical = False
                                        lado_v = 'I'

                                elif tipo_r_v == '˄':

                                    # Si cumple con esa restricción
                                    if valor > int(tiles[fila - 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = tipo_r_v
                                        cumple_vertical = False
                                        lado_v = 'I'

                                # Si no hay restricción se pasa
                                else:
                                    pass

                        # Si no esta ni en la primera ni última fila
                        else:
                            restric_superior = restricciones_verticales[fila - 1][columna]['text']
                            restric_inferior = restricciones_verticales[fila][columna]['text']

                            # Si el cuadro arriba esta vacío
                            if tiles[fila-1][columna]['text'] == '':
                                pass

                            else:

                                # Si hay una relación de mayor que horizontal
                                if restric_superior == 'V':

                                    # Si cumple con esa restricción
                                    if valor < int(tiles[fila - 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = restric_superior
                                        cumple_vertical = False
                                        lado_v = 'I'

                                elif restric_superior == '˄':

                                    # Si cumple con esa restricción
                                    if valor > int(tiles[fila - 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = restric_superior
                                        cumple_vertical = False
                                        lado_v = 'I'

                                # Si no hay restricción se pasa
                                else:
                                    pass

                            if tiles[fila + 1][columna]['text'] == '':
                                pass

                            else:

                                # Si hay una relación de mayor que horizontal
                                if restric_inferior == 'V':

                                    # Si cumple con esa restricción
                                    if valor > int(tiles[fila + 1][columna]['text']):
                                       pass

                                    else:
                                        relacion_no_cumplida_ver = restric_inferior
                                        cumple_vertical = False
                                        lado_v = 'S'

                                elif restric_inferior == '˄':
                                    # Si cumple con esa restricción

                                    if valor < int(tiles[fila + 1][columna]['text']):
                                        pass

                                    else:
                                        relacion_no_cumplida_ver = restric_inferior
                                        cumple_vertical = False
                                        lado_v = 'S'

                                # Si no hay restricción se pasa
                                else:
                                    pass

                        # Si tras revisar todo no se cumple verticalmente
                        if cumple_vertical == False:
                            boton.config(bg='red')
                            regresar_invalidez_vertical(boton, relacion_no_cumplida_ver, lado_v)

                        else:
                            # Se agrega la jugada a la lista
                            # Se agrega el valor pasado y la fila y columna del botón
                            lista_jugadas.append((boton['text'],fila,columna))

                            # Luego de agregar la jugada se modifica el valor del botón
                            boton.config(text = valor)

                            # Se va a revisar si ya se agregaro todos los valores para los botones, si sucede el caso
                            # Se desabilitan los botones y se despliega un mensaje de felicitación
                            todos_completos = True

                            for f_boton in tiles:
                                if todos_completos == False:
                                    break
                                else:
                                    for bo in f_boton:
                                        if bo['text'] == '':
                                            todos_completos = False
                                            break

                            # Si todos están completos, se desabilitan los botones del juego
                            if todos_completos == True:
                                d_1.config(state = 'disabled')
                                d_2.config(state = 'disabled')
                                d_3.config(state = 'disabled')
                                d_4.config(state = 'disabled')
                                d_5.config(state = 'disabled')

                                # Se deshabilita cada boton en la lista de tiles
                                for sa in tiles:
                                    for l in sa:
                                        l.config(state = 'disabled')

                                # Se deshabilitan los botones terminar juego, borrar juego, borrar jugada, guardar juego y se detiene el timer
                                gj.config(state = 'disabled')
                                erase_game.config(state = 'disabled')
                                finish.config(state = 'disabled')
                                erase.config(state = 'disabled')

                                # Se despliega un mensaje de felicitación
                                messagebox.showinfo('Felicidades!', 'Excelente!, Juego terminado con éxito!',master= futoshiki)

                                # Se detiene el reloj
                                terminar_reloj.set('Si')

                                # Se verifica si se agrega al top 10
                                # Para esto primero se define la hora final
                                hora_final = datetime.now()

                                # Se define la diferencia entre la hora inicial y la final para saber el tiempo tomado
                                global tiempo_inicial
                                tiempo_tomado = hora_final - tiempo_inicial

                                # Se convierte a segundos
                                tiempo_tomado = tiempo_tomado.seconds

                                # Se va a calcular las horas, minutos y segundos tomados
                                minutos_jug = tiempo_tomado // 60
                                tiempo_tomado %= 60
                                horas_jug = minutos_jug // 60
                                minutos_jug %= 60
                                segundos_jug = tiempo_tomado

                                # Se forma un tiempo con esos datos
                                x = time(horas_jug,minutos_jug,segundos_jug)

                                # Se van a revisar los recórds en esa dificultad
                                if dificultad.get() == 'Facil':

                                    if top_10[0] == []:
                                        top_10[0].append((nombre_jugador.get(), x.strftime('%H:%M:%S')))

                                    else:
                                        for rec in range(len(top_10[0])):
                                            record = top_10[0][rec][1]

                                            tiempo = datetime.strptime(record, '%H:%M:%S')

                                            tiempo = tiempo.time()

                                            if x > tiempo:
                                                pass

                                            else:

                                                # Se inserta en ese índice
                                                top_10[0].insert(rec, (nombre_jugador.get(), x.strftime('%H:%M:%S')))

                                                # Se corta el top 10 a tener solo 10 valores
                                                top_10[0] = top_10[0][:9]

                                elif dificultad.get() == 'Dificil':

                                    if top_10[2] == []:
                                        top_10[2].append((nombre_jugador.get(), x.strftime('%H:%M:%S')))

                                    else:
                                        for rec in range(len(top_10[2])):
                                            record = top_10[2][rec][1]

                                            tiempo = datetime.strptime(record, '%H:%M:%S')

                                            tiempo = tiempo.time()

                                            if x > tiempo:
                                                pass

                                            else:

                                                # Se inserta en ese índice
                                                top_10[2].insert(rec, (nombre_jugador.get(), x.strftime('%H:%M:%S')))

                                                # Se corta el top 10 a tener solo 10 valores
                                                top_10[2] = top_10[2][:9]

                                else:
                                    if top_10[1] == []:
                                        top_10[1].append((nombre_jugador.get(), x.strftime('%H:%M:%S')))

                                    else:
                                        se_inserto = False
                                        for rec in range(len(top_10[1])):
                                            record = top_10[1][rec][1]

                                            tiempo = datetime.strptime(record, '%H:%M:%S')

                                            tiempo = tiempo.time()

                                            if x > tiempo:
                                                pass

                                            else:
                                                # Se inserta en ese índice
                                                top_10[1].insert(rec, (nombre_jugador.get(), x.strftime('%H:%M:%S')))
                                                se_inserto = True

                                        if se_inserto == True:

                                            if len(top_10[1]) >= 10:
                                                # Se corta el top 10 a tener solo 10 valores
                                                top_10[1] = top_10[1][:9]

                                            else:
                                                pass

                                        else:
                                            if len(top_10[1]) >= 10:
                                                pass

                                            else:
                                                top_10[1].insert(-1, (nombre_jugador.get(), x.strftime('%H:%M:%S')))

    # Función 3 (Borrar jugada)
    # Funciona de acuerdo a la lista de jugadas
    # Verifica si la lista de jugadas ya tiene una registrada de lo contrario retorna error

    # Si hay jugadas y se ejecuta la función
    # Se va a sacar el último valor de la lista de jugadas y se lo va a devolver al botón en ese índice y columna
    def borrar_jugada():

        # Si la lista esta vacía ya no hay jugadas por borrar
        if lista_jugadas == []:
            messagebox.showwarning('Atención!', 'Ya no hay más jugadas por borrar',master= futoshiki)

        # Si aún quedan jugadas por borrar
        else:

            # Se saca el último valor que entro a la lista LIFO
            jugada_pasada = lista_jugadas.pop(-1)

            # Se retorna ese valor pasado a el botón al que pertenecía
            tiles[jugada_pasada[1]][jugada_pasada[2]].config(text = jugada_pasada[0])

    # Función 4 (Terminar Juego)
    # Presenta al usuario con un messagebox con dos opciones
    # Si se marca si (yes) se cierra la ventana jugar y se abre una nueva
    # Si se marca no la ventana no cierra ni tampoco sucede nada

    def terminar_juego():
        mensaje = messagebox.askquestion('Terminar Juego', '¿Esta seguro de terminar el juego?',master= futoshiki)

        if mensaje == 'yes':
            # Se cierra la ventana
            futoshiki.destroy()

            # Se vuelve a ejecutar la función para abrir un juego nuevo
            jugar_futoshiki([])

        # Si el mensaje es no, se cierra el mensaje y se regresa
        else:
            pass

    # Función 5 (Borrar Juego)
    # Le presenta al usuario un mensaje donde se le pregunta si esta seguro de borrar el juego
    # Si marca no, se cierra el mensaje y no pasa nada
    # Si marca que si, todas las jugadas hechas se reinician y el mapa vuelve a ser como era al principio
    def borrar_juego():

        mensaje_borrar = messagebox.askquestion('Borrar Juego', '¿Esta seguro de borrar el juego?',master= futoshiki)

        # Si se indica borrar se van a borrar todos los valores en los botones que no son fijos
        if mensaje_borrar == 'yes':

            # Se vacía la lista de jugadas
            lista_jugadas.clear()

            # Se buscan todos los tiles, si no son fijos se vacían
            for v in tiles:
                for vb in v:

                    if vb['state'] == 'disabled':
                        pass

                    else:
                        vb.config(text = '')

        # Si el mensaje es no, se cierra el mensaje y se regresa
        else:
            pass

    # Para las variables importantes
    # Número actual seleccionado por los botones de dígitos
    # Comienza como ninguno

    numero_actual = tk.StringVar()
    numero_actual.set('')

    # Nombre del jugador
    nombre_jugador = tk.StringVar()
    nombre_jugador.set('')

    # Variable para el tiempo de inicio
    tiempo_inicial = ''

    # Variable para detener el reloj / timer
    terminar_reloj = tk.StringVar()
    terminar_reloj.set('No')

    # Info ventana
    futoshiki.title("FUTOSHIKI -- Buena Suerte!")
    futoshiki.geometry('850x850')

    # Lista de Jugadas
    # Comienza como vacía y se le van agreganndo jugadas conforma
    # Al presionar el botón cargar juego se le asigna las jugadas de la partida pasada
    lista_jugadas = []

    if cargado != []:
        lista_jugadas = cargado[0]

    # Para el reloj / contador
    # Si se debe desplegar el reloj
    if reloj.get() != 'No':

        #Labels
        hr = tk.Label(futoshiki, text='Horas', font=('Times New Roman', 12),relief = 'solid', bg = 'white', width = 6)
        hr.place(x=642, y=30)

        min = tk.Label(futoshiki, text='Minutos', font=('Times New Roman', 12),relief = 'solid', bg = 'white', width = 7)
        min.place(x=700, y=30)

        sec = tk.Label(futoshiki, text='Segundos', font=('Times New Roman', 12),relief = 'solid', bg = 'white', width = 7)
        sec.place(x= 767, y=30)

        # Tiempo
        # Se determinan dependiendo de la configuración
        horas = tk.IntVar()
        horas.set(00)

        minutos = tk.IntVar()
        minutos.set(00)

        segundos = tk.IntVar()
        segundos.set(00)

        # En caso de estar seleccionada la opción timer
        if reloj.get() == 'Timer':

            # Se les da los valores del timer
            horas.set(int(horas_timer.get()))
            minutos.set(int(minutos_timer.get()))
            segundos.set(int(segundos_timer.get()))

        if cargado != []:

            horas.set(cargado[2][2][0])
            minutos.set(cargado[2][2][1])
            segundos.set(cargado[2][2][2])

        # Se hacen labels con estos
        horas_display = tk.Label(futoshiki, text= horas.get(), font=('Times New Roman', 12), relief='solid', bg='white', width=6, height = 2)
        horas_display.place(x=642, y=54)

        minutos_display = tk.Label(futoshiki, text=minutos.get(), font=('Times New Roman', 12), relief='solid', bg='white',width=7, height=2)
        minutos_display.place(x=700, y=54)

        segundos_display = tk.Label(futoshiki, text=segundos.get(), font=('Times New Roman', 12), relief='solid',bg='white', width=7, height=2)
        segundos_display.place(x=767, y=54)

    # Labels y botones
    tuit = tk.Label(futoshiki,relief = 'solid',bg = 'PURPLE', fg = 'YELLOW',text = 'FUTOSHIKI', font = ('Times New Roman', 40))
    tuit.place(x = 260, y = 10)

    ni = tk.Label(futoshiki,text = 'Nivel  ' + str(dificultad.get()), font = ('Times New Roman', 18))
    ni.place(x = 330, y = 90)

    ni = tk.Label(futoshiki, text='Nombre del Jugador: ', font=('Times New Roman', 18))
    ni.place(x= 30, y=140)

    playername = tk.Entry(futoshiki,font=('Times New Roman', 18), width = 35)
    playername.place(x=270, y=140)

    if cargado != []:
        playername.delete(0,'end')
        playername.insert(0,cargado[2][1])

    # Botones de dígitos
    d_1 = tk.Radiobutton(futoshiki, text='1', font=('Times New Roman', 18), width = 4, background = "azure", activebackground='light blue',activeforeground='black',
                         indicator = 0, value='1', variable= numero_actual,state = 'disabled',disabledforeground = 'grey')

    d_2 = tk.Radiobutton(futoshiki, text='2', font=('Times New Roman', 18), width = 4, background = "azure", activebackground='light blue',activeforeground='black',
                         indicator = 0, value='2', variable= numero_actual,state = 'disabled',disabledforeground = 'grey')

    d_3 = tk.Radiobutton(futoshiki, text='3', font=('Times New Roman', 18), width = 4,  background = "azure", activebackground='light blue',activeforeground='black',
                         indicator = 0, value='3', variable= numero_actual,state = 'disabled',disabledforeground = 'grey')

    d_4 = tk.Radiobutton(futoshiki, text='4', font=('Times New Roman', 18), width = 4, background = "azure",indicator = 0, activebackground='light blue',activeforeground='black',
                           value='4', variable= numero_actual,state = 'disabled',disabledforeground = 'grey')

    d_5 = tk.Radiobutton(futoshiki, text='5', font=('Times New Roman', 18), width = 4,  background = "azure",activebackground='light blue',activeforeground='black',
                         indicator = 0, value='5', variable= numero_actual,state = 'disabled',disabledforeground = 'grey')

    # Se colocan dependiendo de la configuración
    if position.get() == 'Derecha':
        d_1.place(x = 720, y = 220)
        d_2.place(x=720, y=320)
        d_3.place(x=720, y= 420)
        d_4.place(x=720, y=520)
        d_5.place(x=720, y=620)

    else:
        d_1.place(x = 40, y = 220)
        d_2.place(x=40, y=320)
        d_3.place(x= 40, y=420)
        d_4.place(x=40, y=520)
        d_5.place(x=40, y=620)

    # Se crean 25 botones distintos para cada uno de los marcos del futoshiki
    lab_0_0 = tk.Button(futoshiki,text = '', font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_0_0))
    lab_0_0.place(x = 180, y = 210)

    lab_0_1 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_0_1))
    lab_0_1.place(x = 280, y = 210)

    lab_0_2 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_0_2))
    lab_0_2.place(x=380, y=210)

    lab_0_3 = tk.Button(futoshiki, text='', font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_0_3))
    lab_0_3.place(x=480, y=210)

    lab_0_4 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_0_4))
    lab_0_4.place(x=580, y=210)

    lab_1_0 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_1_0))
    lab_1_0.place(x = 180, y = 310)

    lab_1_1 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_1_1))
    lab_1_1.place(x = 280, y = 310)

    lab_1_2 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_1_2))
    lab_1_2.place(x=380, y=310)

    lab_1_3 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_1_3))
    lab_1_3.place(x=480, y=310)

    lab_1_4 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_1_4))
    lab_1_4.place(x=580, y=310)

    lab_2_0 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_2_0))
    lab_2_0.place(x = 180, y = 410)

    lab_2_1 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_2_1))
    lab_2_1.place(x = 280, y = 410)

    lab_2_2 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_2_2))
    lab_2_2.place(x=380, y =410)

    lab_2_3 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_2_3))
    lab_2_3.place(x=480, y =410)

    lab_2_4 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_2_4))
    lab_2_4.place(x=580, y =410)

    lab_3_0 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_3_0))
    lab_3_0.place(x = 180, y = 510)

    lab_3_1 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_3_1))
    lab_3_1.place(x = 280, y = 510)

    lab_3_2 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_3_2))
    lab_3_2.place(x=380, y=510)

    lab_3_3 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_3_3))
    lab_3_3.place(x=480, y=510)

    lab_3_4 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_3_4))
    lab_3_4.place(x=580, y=510)

    lab_4_0 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_4_0))
    lab_4_0.place(x = 180, y = 610)

    lab_4_1 = tk.Button(futoshiki,text = '',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_4_1))
    lab_4_1.place(x = 280, y = 610)

    lab_4_2 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_4_2))
    lab_4_2.place(x=380, y=610)

    lab_4_3 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_4_3))
    lab_4_3.place(x=480, y=610)

    lab_4_4 = tk.Button(futoshiki, text='',  font=('Times New Roman', 21, 'bold'),relief = 'solid', bg = 'white', width = 3, height = 1
                        ,state = 'disabled',disabledforeground = 'black',command = lambda: activar_tile(lab_4_4))
    lab_4_4.place(x=580, y=610)

    # Se guardan todos los labels en una lista, esta contendrá cada uno de ellos divididos en columnas y filas
    tiles = [[lab_0_0,lab_0_1,lab_0_2,lab_0_3,lab_0_4], # Fila 1
           [lab_1_0,lab_1_1,lab_1_2,lab_1_3,lab_1_4], # Fila 2
           [lab_2_0,lab_2_1,lab_2_2,lab_2_3,lab_2_4], # Fila 3
           [lab_3_0,lab_3_1,lab_3_2,lab_3_3,lab_3_4], # Fila 4
           [lab_4_0,lab_4_1,lab_4_2,lab_4_3,lab_4_4]] # Fila 5

    # Primero se crean todos los labels como vacíos

    # Para aquellos horizontales
    # Primera fila
    hor_restr_0_0 = tk.Label(futoshiki, text='', font =('Times New Roman', 20, 'bold'))
    hor_restr_0_0.place(x=250, y=223)

    hor_restr_0_1 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_0_1.place(x=350, y=223)

    hor_restr_0_2 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_0_2.place(x=450, y=223)

    hor_restr_0_3 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_0_3.place(x=550, y=223)

    # Segunda fila
    hor_restr_1_0 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_1_0.place(x=250, y=323)

    hor_restr_1_1 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_1_1.place(x=350, y=323)

    hor_restr_1_2 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_1_2.place(x=450, y=323)

    hor_restr_1_3 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_1_3.place(x=550, y=323)

    # Tercera Fila
    hor_restr_2_0 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_2_0.place(x=250, y=423)

    hor_restr_2_1 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_2_1.place(x=350, y=423)

    hor_restr_2_2 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_2_2.place(x=450, y=423)

    hor_restr_2_3 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_2_3.place(x=550, y=423)

    # Cuarta Fila
    hor_restr_3_0 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_3_0.place(x=250, y=523)

    hor_restr_3_1 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_3_1.place(x=350, y=523)

    hor_restr_3_2 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_3_2.place(x=450, y=523)

    hor_restr_3_3 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_3_3.place(x=550, y=523)

    # Quinta Fila
    hor_restr_4_0 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_4_0.place(x=250, y= 623)

    hor_restr_4_1 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_4_1.place(x=350, y=623)

    hor_restr_4_2 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_4_2.place(x=450, y=623)

    hor_restr_4_3 = tk.Label(futoshiki, text='', font=('Times New Roman', 20, 'bold'))
    hor_restr_4_3.place(x=550, y=623)

    # Se guardan estos labels en una lista
    restricciones_horizontales = [[hor_restr_0_0,hor_restr_0_1,hor_restr_0_2,hor_restr_0_3],
                                  [hor_restr_1_0,hor_restr_1_1,hor_restr_1_2,hor_restr_1_3],
                                  [hor_restr_2_0,hor_restr_2_1,hor_restr_2_2,hor_restr_2_3],
                                  [hor_restr_3_0,hor_restr_3_1,hor_restr_3_2,hor_restr_3_3],
                                  [hor_restr_4_0,hor_restr_4_1,hor_restr_4_2,hor_restr_4_3]]

    # Estos labels se van a modificar según los requisitos del mapa que indiquen restricciones de tipo '>' o '<'
    # Por cada restricción, si se encuentra una comparación horizontal se cambia el índice al que pertenece
    for restriccion in mapa:
        if restriccion[0] == ">" or restriccion[0] == "<":
            restricciones_horizontales[restriccion[1]][restriccion[2]].config(text = restriccion[0])

    # Luego se crean los Labels para las restricciones verticales
    # Primera fila
    ver_restr_0_0 = tk.Label(futoshiki, text='', font =(20))
    ver_restr_0_0.place(x=200, y=268)

    ver_restr_0_1 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_0_1.place(x=300, y=268)

    ver_restr_0_2 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_0_2.place(x=400, y=268)

    ver_restr_0_3 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_0_3.place(x=500, y=268)

    ver_restr_0_4 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_0_4.place(x=600, y=268)

    # Segunda fila
    ver_restr_1_0 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_1_0.place(x=200, y=368)

    ver_restr_1_1 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_1_1.place(x=300, y=368)

    ver_restr_1_2 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_1_2.place(x=400, y=368)

    ver_restr_1_3 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_1_3.place(x=500, y=368)

    ver_restr_1_4 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_1_4.place(x=600, y=368)

    # Tercera fila
    ver_restr_2_0 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_2_0.place(x=200, y=468)

    ver_restr_2_1 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_2_1.place(x=300, y=468)

    ver_restr_2_2 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_2_2.place(x=400, y=468)

    ver_restr_2_3 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_2_3.place(x=500, y=468)

    ver_restr_2_4 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_2_4.place(x=600, y=468)

    # Cuarta Fila
    ver_restr_3_0 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_3_0.place(x=200, y=568)

    ver_restr_3_1 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_3_1.place(x=300, y=568)

    ver_restr_3_2 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_3_2.place(x=400, y=568)

    ver_restr_3_3 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_3_3.place(x=500, y=568)

    ver_restr_3_4 = tk.Label(futoshiki, text='', font=(20))
    ver_restr_3_4.place(x=600, y=568)


    restricciones_verticales = [[ver_restr_0_0,ver_restr_0_1,ver_restr_0_2,ver_restr_0_3,ver_restr_0_4],
                                [ver_restr_1_0,ver_restr_1_1,ver_restr_1_2,ver_restr_1_3,ver_restr_1_4],
                                [ver_restr_2_0,ver_restr_2_1,ver_restr_2_2,ver_restr_2_3,ver_restr_2_4],
                                [ver_restr_3_0,ver_restr_3_1,ver_restr_3_2,ver_restr_3_3,ver_restr_3_4]]

    # Estos labels se van a modificar según los requisitos del mapa que indiquen restricciones de tipo 'V' o '^'
    # Por cada restricción, si se encuentra una comparación vertical se cambia el índice al que pertenece
    for restriccion in mapa:
        if restriccion[0] == '˄' or restriccion[0] == 'V':
            restricciones_verticales[restriccion[1]][restriccion[2]].config(text=restriccion[0])


    # Para los números fijos
    for restriccion in mapa:
        if restriccion[0].isdigit():
            tiles[restriccion[1]][restriccion[2]].config(text = restriccion[0])

    # En caso de que se cargara un mapa pasado se importan los valores de los tiles
    if cargado != []:
        for fi in cargado[3]:
            for ci in fi:
                tiles[ci[1]][ci[2]].config(text =ci[0])

    # Se crean el resto de botones
    # Iniciar Juego
    startgame = tk.Button(futoshiki,text= 'Iniciar \n Juego', bg = "purple", fg = 'white', width = 10, font = (14),disabledforeground = 'grey',command = iniciar_juego)
    startgame.place(x = 50, y = 700)

    # Borrar jugada
    erase = tk.Button(futoshiki,text= 'Borrar \n Jugada', bg = "purple", fg = 'white',  width = 10, font = (14)
                      ,state = 'disabled',disabledforeground = 'grey',command = borrar_jugada)
    erase.place(x =210, y = 700)

    # Terminar Juego
    finish = tk.Button(futoshiki, text='Terminar \n Juego', bg="purple", fg='white', width=10, font=(14)
                       ,state = 'disabled',disabledforeground = 'grey', command = terminar_juego)
    finish.place(x=370, y=700)

    # Borrar Juego
    erase_game = tk.Button(futoshiki, text='Borrar \n Partida', bg="purple", fg='white', width=10, font=(14)
                           ,state = 'disabled',disabledforeground = 'grey', command = borrar_juego)
    erase_game.place(x=530, y=700)

    # Top 10
    tp = tk.Button(futoshiki, text='Top \n 10', bg="purple", fg='white', width=10, font=(14),command = abrir_top)
    tp.place(x=690, y=700)

    # Guardar Juego
    gj = tk.Button(futoshiki, text = 'Guardar Juego', relief ='solid', font=(16),width = 14, state = 'disabled', disabledforeground = 'grey'
                   ,command = guardar_juego)
    gj.place(x =450, y = 780)

    # Cargar Juego
    cj = tk.Button(futoshiki, text='Cargar Juego', relief='solid', font=(16), width=14,command = cargar_juego)
    cj.place(x=650, y=780)

# Función de cierre
# Guarda datos y cierra la ventana principal
def cierre():

    # Para guardar la configuración
    salvar_config = open('futoshiki2021configuración.dat','wb')

    datos_config = [dificultad.get(),reloj.get(),position.get(),int(horas_timer.get()),int(minutos_timer.get()),int(segundos_timer.get())]

    pickle.dump(datos_config,salvar_config)
    salvar_config.close()

    # Para guardar el top10
    guardar_top10 = open('futoshiki2021top10.dat','wb')

    pickle.dump(top_10, guardar_top10)
    guardar_top10.close()

    principal_futoshiki.destroy()

#=======================================================================================================================
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
jugar = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='JUGAR', font=('Times New Roman', 25), command = lambda: jugar_futoshiki([]))
jugar.place(x = 295, y = 160)

configurar = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='CONFIGURAR', font=('Times New Roman', 25),
                       command = configuracion)
configurar.place(x = 245, y = 280)

ayuda = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='AYUDA', font=('Times New Roman', 25),command = lambda: os.system('manual_de_usuario_futoshiki.pdf'))
ayuda.place(x = 295, y = 390)

Salir = tk.Button(principal_futoshiki, fg = 'black', relief = 'solid',  text ='SALIR', font=('Times New Roman', 25),command = cierre)
Salir.place(x = 305, y = 500)

principal_futoshiki.protocol("WM_DELETE_WINDOW", cierre)

principal_futoshiki.mainloop()
