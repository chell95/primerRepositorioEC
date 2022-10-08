class Ahorcado:
    
    def __init__(self):
        self.dibujo = [
        '''  
             ***********
             *         *
                       *
                       *
                       *
            ************''',
        '''  
             ***********
             *         *
             O         *
                       *
                       *
            ************''',
        '''  
             ***********
             *         *
             O         *
             |         *
                       *
            ************''',
        '''  
             ***********
             *         *
             O         *
            /|         *
                       *
            ************''',
        '''  
             ***********
             *         *
             O         *
            /|\        *
                       *
            ************''',
        '''  
             ***********
             *         *
             O         *
            /|\        *
            /          *
            ************''',
        '''  
             ***********
             *         *
             O         *
            /|\        *
            / \        *
            ************''']

    def obtieneDibujo(self, vidas):
        """obtieneDibujo

        Args:
            vidas (int): el nuemero de intentos

        Returns:
            int: retornamos el numero de vidas que nos queda por cada intento.
        """
        return self.dibujo[self.getTotalVidas() - vidas]

    def getTotalVidas(self):
        """getTotalVidas

        Returns:
            list: Retorna el ahorcado dependiendo de las vidas perdidas 
        """
        return int(len(self.dibujo)-1)