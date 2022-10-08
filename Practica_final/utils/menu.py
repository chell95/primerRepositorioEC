class Menu:
    def __init__(self):
        self.encabezado = "======================================="

    def opts(self,titulo, *opt, **mensajes):
        mensajes.setdefault("primera_vez", True)
        mensajes.setdefault("error", "Opcion no existe")
        if mensajes["primera_vez"]:
            titulo = "::  BIENVENIDO al " + titulo + "  :: "
            print(self.encabezado)
            print(titulo)
            print(self.encabezado)
        else:
            titulo = "::  " + titulo + "  :: "
            print(self.encabezado)
            print(titulo)
            print(self.encabezado)

        for i in range(len(opt)):
            print(f"{i+1}.- {opt[i]}")
        opc = int(input("Selecciona una opción:  "))
        if opc >= 1 and opc <= len(opt):
            return opc
        else:
            print(mensajes["error"])
            return -1