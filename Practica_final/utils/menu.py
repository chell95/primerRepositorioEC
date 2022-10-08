class Menu:
    def __init__(self):
        self.encabezado = "======================================="

    def opts(self,titulo:str, *opt:int, **mensajes:bool)->int:
        """opts

        Args:
            titulo (srt): El titulo del juego
            opts (int): las opciones que se tiene del menu
            mensajes (bool): la bandera
            

        Returns:
            int: retorna la opcion del menu o en su caso -1
        """
        mensajes.setdefault("primera_vez", True)
        mensajes.setdefault("error", "Opcion no existe")
        if mensajes["primera_vez"]:
            titulo = "::  BIENVENIDO a " + titulo + "  :: "
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