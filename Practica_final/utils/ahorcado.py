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
             0         *
                       *
                       *
            ************''',
        '''  
             ***********
             *         *
             0         *
             |         *
                       *
            ************''',
        '''  
             ***********
             *         *
             0         *
            /|         *
                       *
            ************''',
        '''  
             ***********
             *         *
             0         *
            /|\        *
                       *
            ************''',
        '''  
             ***********
             *         *
             0         *
            /|\        *
            /          *
            ************''',
        '''  
             ***********
             *         *
             0         *
            /|\        *
            / \        *
            ************''']

    def obtieneDibujo(self, vidas):
        return self.dibujo[self.getTotalVidas() - vidas]

    def getTotalVidas(self):
        return int(len(self.dibujo))