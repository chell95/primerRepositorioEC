import os

from utils.ahorcado import Ahorcado
from utils.menu import Menu
from models.palabra import Palabra


def main():
    menuPrincial = Menu()
    dibujo = Ahorcado()
    palabraN = Palabra()

    bandera = True
    while True:
        vidas = dibujo.getTotalVidas()
        opt = menuPrincial.opts("Juguemos al AHORCADO", "Comenzar",
                  "Salir", primera_vez=bandera)
        if opt == 1:
            #os.system('cls')
            while palabraN.igualaListas() != True and vidas > 0:
                print(dibujo.obtieneDibujo(vidas))
                print(palabraN.mostraPalabraGuion())
                opt = input("Ingresa la letra: ")
                if palabraN.addLetra(opt) == False:
                    vidas = vidas - 1
            if vidas == 0:
                print  ("PERDISTE La palabra a adivinar era:  ")
                print("".join(palabraN.mostrarPalabra()))
                print(dibujo.obtieneDibujo(vidas))  
            else:
                print("Has adivinado la palabra FELICIDADES!!!") 
                print("".join(palabraN.mostrarPalabra()))          
        elif opt == 2:
            break
        else:
            bandera = False

if __name__ == "__main__":
    main()