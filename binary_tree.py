from Nodulo import Nodulo


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        Nodulo = Nodulo(value)
        if self.root is None:
            self.root = Nodulo
        else:
            aux = self.root
            while (True):
                if (aux.value >= value):
                    Rcima = aux
                    aux = aux.getEsquerda()
                    Rbaixo = True

                else:
                    Rcima = aux
                    aux = aux.getDireita()
                    Rbaixo = False

                if (aux is None):
                    break
                if Rbaixo is False:
                    Rcima.set_dir(Nodulo)
                else:
                    Rcima.set_esq(Nodulo)

    def achar(self, value):
        if value < self.value:
            if self.esquerda is None:
                return False
            else:
                return self.esquerda.achar(value)
        elif value > self.value:
            if self.direita is None:
                return False
            else:
                return self.direita.achar(value)

    def remover(self, value: int):
        if self.root is None:
            return False
    
        elif self.root.value == value:
            if (self.root.get_dir() is None and self.root.get_dir() is None):
                self.root = None
            elif (self.root.get_esq() and self.root.get_dir() is None):
                self.root = self.root.get_esq()
            elif (self.root.get_esq() is None and self.root.get_dir()):
                self.root = self.root.get_dir()
            elif (self.root.get_esq() and self.root.get_dir()):

                AuxNoduloTopo = self.root      
                removerNodulo: Nodulo = self.root.get_dir()     #

                while (removerNodulo.get_esq()):
                    AuxNoduloTopo = removerNodulo
                    removerNodulo = removerNodulo.get_esq()

                self.root.value = removerNodulo.value
                if removerNodulo.get_dir():
                    if AuxNoduloTopo.value > removerNodulo.value:
                        AuxNoduloTopo.set_esq(removerNodulo.get_dir())
                    elif AuxNoduloTopo.value < removerNodulo.value:
                        AuxNoduloTopo.set_dir(removerNodulo.get_dir())
                else:
                    if removerNodulo.value < AuxNoduloTopo.value:
                        AuxNoduloTopo.set_esq(None)
                    else:
                        AuxNoduloTopo.set_dir(None)
            return True

        new_Rbaixo = None  
        Nodulo = self.root

        while Nodulo and Nodulo.value != value:
            new_Rbaixo = Nodulo
            if value < Nodulo.value:
                Nodulo = Nodulo.get_esq()
            elif value > Nodulo.value:
                Nodulo = Nodulo.get_dir()


        if Nodulo is None or Nodulo.value != value:
            return False

        elif Nodulo.get_esq() is None and Nodulo.get_dir() is None:
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(None)
            else:
                new_Rbaixo.set_dir(None)
            return True

   
        elif Nodulo.get_esq() and Nodulo.get_dir() is None:
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(Nodulo.get_esq())
            else:
                new_Rbaixo.set_dir(Nodulo.get_esq())
            return True

        elif Nodulo.get_esq() is None and Nodulo.get_dir():
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(Nodulo.get_dir())
            else:
                new_Rbaixo.set_dir(Nodulo.get_dir())
            return True
        
        else:
            AuxNoduloTopo = Nodulo
            removerNodulo = Nodulo.get_dir()
            while removerNodulo.get_esq():
                AuxNoduloTopo = removerNodulo
                removerNodulo = removerNodulo.get_esq()
            Nodulo.value = removerNodulo.value
            if removerNodulo.get_dir():
                if AuxNoduloTopo.value > removerNodulo.value:
                    AuxNoduloTopo.set_esq(removerNodulo.get_dir())
                elif AuxNoduloTopo.value < removerNodulo.value:
                    AuxNoduloTopo.set_dir(removerNodulo.get_dir())
            else:
                if removerNodulo.value < AuxNoduloTopo.value:
                    AuxNoduloTopo.set_esq(None)
                else:
                    AuxNoduloTopo.set_dir(None)

    def pre_ordem(self):
        if self.root is not None:
            self.root.pre_ordem()

    def em_ordem(self):
        if self.root is not None:
            self.root.em_ordem()

    def pos_ordem(self):
        if self.root is not None:
            self.root.pos_ordem()

    def print_bt(self):
        print("Arvore Pré-Ordem: ")
        print(self.pre_ordem())
        print("Arvore Em-Ordem: ")
        print(self.em_ordem())
        print("Arvore Pós-Ordem:")
        print(self.pos_ordem())