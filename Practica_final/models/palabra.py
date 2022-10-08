import random as r

class Palabra:


    def __init__(self):
        self.lsPalabras = ["Natacion", "Tradicion", "Mazapan", "Secreto", "Secretaria", "Corazon", "Leopardo", "Tortilla",
         "Tormenta", "Moraleja", "Tornado", "Tamarindo","Rinoceronte", "Carretera", "Cocina", "Ahorcado", "Territorio"]
        self.palabra = self.lsPalabras[r.randint(0,(len(self.lsPalabras)-1))]
        self.adivina = ["_" for i in range(len(self.palabra))] 
    

    def addLetra(self, letra):
        if str(letra).lower() in self.palabra or str(letra).upper() in self.palabra:
            for i in range(len(self.palabra)):
                if list(self.palabra)[i].upper() == str(letra).upper():
                    self.adivina[i] = list(self.palabra)[i]
        else:
            print(self.adivina)
            return False
        print(self.adivina)
        return True

    def igualaListas(self):
        return ("".join(self.adivina) == self.palabra)
    
    def existePalabra(self, pl):
        return (str(pl).lower() in self.adivina or str(pl).upper() in self.adivina)


'''n = Palabra()

while n.igualaListas() != True:
    opt = input("Ingresa la letra: ")
    n.addLetra(opt)
'''