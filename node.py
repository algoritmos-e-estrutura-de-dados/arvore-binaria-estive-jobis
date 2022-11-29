class Node:

    def __init__(self, value, direita = None, esquerda = None):
        self.value = value
        self.direita = direita
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda
    
    def getDireita(self):
        return self.direita
    
    def getEsquerda(self):
        return self.esquerda
    
    def procurar(self, busca: int):
        if (self.value == busca):
            return True

        elif self.value > busca:
            if self.esquerda:
                return self.esquerda.procurar(busca)
            else:
                return False

        else:
            if self.direita:
                return self.direita.procurar(busca)
            else:
                return False
    
    def Print(self):
        if self:
            if self.esquerda:
                self.esquerda.em_ordem()
            print (str(self.value))
            if self.direita:
                self.direita.em_ordem()

            
    