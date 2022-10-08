import os

from utils.ahorcado import Ahorcado
from utils.menu import Menu
from models.palabra import Palabra


def main():
    menuPrincial = Menu()
    dibujo = Ahorcado()
    palabraN = Palabra()
    vidas = dibujo.getTotalVidas()

    bandera = True
    while True:
        #os.system('cls')
        opt = menuPrincial.opts("Juego del ahorcado", "Comenzar",
                  "Visualizar marcador", "Salir", primera_vez=bandera)
        if opt == 1:
            #os.system('cls')
            while palabraN.igualaListas() != True and vidas > 0:
                print(dibujo.obtieneDibujo(vidas))
                opt = input("Ingresa la letra: ")
                if palabraN.addLetra(opt) == False:
                    vidas = vidas - 1                
        elif opt == 3:
            break
        else:
            bandera = False

if __name__ == "__main__":
    main()