from tkinter import *
import random

#---VARIABLES
tamanio = 10
matRango = range(tamanio)
matMapa = [[0 for x in matRango] for y in matRango] #---matMapa[y][x]
matInterfaz = [[None for x in matRango] for y in matRango]
bombas = tamanio - 1
banderasPuestas = 0
final = False
bandera = []
buscado = []
ubiBomb = []

raiz = Tk()
imaBomba = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\bomb.png")
imaFlor = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\flor.png")
imaCero = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\zero.png")
imaUno = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\uno.png")
imaDos = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\dos.png")
imaTres = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\tres.png")
imaCuatro = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\cuatro.png")
imaBandera = PhotoImage(file=r"C:\Users\rober\OneDrive\Documentos\Guille\Python\Minesweeper\bandera.png")
raiz.resizable(width=0, height=0)
raiz.title("Buscaminas!")
miFrame = Frame(raiz)
miFrame.pack()

cantBombas = bombas
cantBandera = "Banderas: " + repr(cantBombas)
misBanderas = Label(miFrame,text=cantBandera, font=(12))
misBanderas.grid(pady=3,column=tamanio-3,columnspan=3,row=tamanio)

#---FUNCIONES
while bombas >= 1:
    b = random.randint(0,tamanio - 1)
    a = random.randint(0,tamanio - 1)
    if matMapa[b][a] == 0:
        ubiBomb.append([b,a])
        matMapa[b][a] = 7
        b-= 1
        a-= 1
        bend = b + 3
        aend = a + 3
        while b < (bend):
            if (b >= 0) and (b < tamanio):
                while a < (aend):
                    if (a >= 0) and (a < tamanio):
                        if (matMapa[b][a] != 7): #--- (7) Representa la bomba
                            matMapa[b][a] += 1
                    a+= 1
                a-= 3
            b+= 1
        bombas -= 1

def setBandera(event,fila,columna):
    global cantBombas
    global cantBandera
    global banderasPuestas
    if [fila,columna] not in buscado and final != True:
        if [fila,columna] not in bandera:
            banderasPuestas+= 1
            bandera.append([fila,columna])
            matInterfaz[fila][columna].config(image=imaBandera)
            cantBombas-= 1
            cantBandera = "Banderas: " + repr(cantBombas)
            misBanderas.config(text=cantBandera)
        else:
            banderasPuestas-= 1
            bandera.remove([fila,columna])
            matInterfaz[fila][columna].config(image=imaCero)
            cantBombas+= 1
            cantBandera = "Banderas: " + repr(cantBombas)
            misBanderas.config(text=cantBandera)
 
def mostrarCasilla(fila, columna):
    global buscado
    global ubiBomb
    global cantBandera
    global final
    bombas = tamanio - 1
    if [fila,columna] not in buscado and [fila,columna] not in bandera and final != True:
        if matMapa[fila][columna] == 0:
            buscado.append([fila,columna])
            matInterfaz[fila][columna].config(relief=SUNKEN, image=imaCero)
            if fila - 1 >= 0 and columna - 1 >= 0:
                mostrarCasilla(fila - 1, columna - 1)
            if fila - 1 >= 0:
                mostrarCasilla(fila - 1, columna)
            if fila - 1 >= 0 and columna + 1 < tamanio:
                mostrarCasilla(fila - 1, columna + 1)
            if columna - 1 >= 0 :
                mostrarCasilla(fila, columna - 1)
            if columna + 1 < tamanio:
                mostrarCasilla(fila, columna + 1)
            if fila + 1 < tamanio and columna - 1 >= 0:
                mostrarCasilla(fila + 1, columna - 1)
            if fila + 1 < tamanio:
                mostrarCasilla(fila + 1, columna)
            if fila + 1 < tamanio and columna + 1 < tamanio:
                mostrarCasilla(fila + 1, columna + 1)
        else:
            if matMapa[fila][columna] != 7:
                if matMapa[fila][columna] == 1:
                    matInterfaz[fila][columna].config(relief=SUNKEN, image=imaUno)
                if matMapa[fila][columna] == 2:
                    matInterfaz[fila][columna].config(relief=SUNKEN, image=imaDos)
                if matMapa[fila][columna] == 3:
                    matInterfaz[fila][columna].config(relief=SUNKEN, image=imaTres)
                if matMapa[fila][columna] == 4:
                    matInterfaz[fila][columna].config(relief=SUNKEN, image=imaCuatro)
                buscado.append([fila,columna])
            else:
                for num1 in ubiBomb:
                    matInterfaz[num1[0]][num1[1]].config(relief=SUNKEN, image=imaBomba)
                final = True
                cantBandera = "Perdiste"
                misBanderas.config(text=cantBandera)

    if ((tamanio*tamanio) - bombas) == len(buscado):
        for num1 in ubiBomb:
            matInterfaz[num1[0]][num1[1]].config(image=imaFlor)
        final = True
        cantBandera = "Ganaste"
        misBanderas.config(text=cantBandera)

#---INTERFAZ
for j in matRango:
    for i in matRango:
        matInterfaz[j][i] = Button(miFrame, image=imaCero, command=lambda fila=j, columna=i: mostrarCasilla(fila, columna))
        matInterfaz[j][i].bind("<Button-3>",lambda event,fila=j, columna=i: setBandera(event, fila, columna))
        matInterfaz[j][i].grid(row=j, column=i)
raiz.mainloop()