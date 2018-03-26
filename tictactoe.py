#Librerias

#Variables
xSymb = "X"
mSymb = "⦿"
totTurn = 9
lastTurn = 0
playerPosY = 0
playerPosX = 0
playerSym = ""
playerOpt = 0
symSelect = False
control = False

desk = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

#Funciones

def printDesk ():
    for i in range(0,3):
        fila = ""
        for j in range(0,3):
            fila += desk[i][j]
        print (fila)


#Selección de símbolo
while symSelect == False:

    playerOpt = input("0 para usar X, 1 para usar ⦿: ")
    playerOpt = int(playerOpt)

    if playerOpt == 0:
        playerSym = xSymb
        symSelect = True
        print(playerOpt)
    elif playerOpt == 1:
        playerSym = mSymb
        symSelect = True
        print(playerOpt)
    else:
        print("Error")

#Inicio
while lastTurn < totTurn:

    control = False

    while control == False:
        playerPosY = int(input("Introduce la fila (1, 2, 3): "))
        playerPosX = int(input("Introduce la columna (1, 2, 3): "))

        if playerPosY < 4 and playerPosY > 0:
            if playerPosX < 4 and playerPosX > 0:
                control = True
            else:
                print("Fuera de rango columna")
        else:
            print("Fuera de rango fila.")

    if desk[playerPosY-1][playerPosX-1] == "-":
        desk[playerPosY-1][playerPosX-1] = playerSym
        printDesk()
        lastTurn += 1
    else:
        print("Posicion ya escogida.")

