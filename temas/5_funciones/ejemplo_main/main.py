''' importar todas las funciones de funciones'''
#from funciones import *
''' importar todo el archivo y darle un alias'''
import funciones as f

def main():
    print("Hola mundo")
    #maxi,mini = f.maximo_minimo(1,2,3)
    #print(f"maximo = {maxi} , minimo = {mini}")
    #print(suma_n_numeros(2,2,5,6,7,9,1,2))
    print(f.suma_n_numeros(2,2,5,6,7,9,1,2))
    
if __name__ == "__main__":
    main()