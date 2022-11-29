from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = node(value)
        if self.root is None:
            self.root = node
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
                    Rcima.set_dir(node)
                else:
                    Rcima.set_esq(node)

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

                AuxnodeTopo = self.root      
                removernode: node = self.root.get_dir()     #

                while (removernode.get_esq()):
                    AuxnodeTopo = removernode
                    removernode = removernode.get_esq()

                self.root.value = removernode.value
                if removernode.get_dir():
                    if AuxnodeTopo.value > removernode.value:
                        AuxnodeTopo.set_esq(removernode.get_dir())
                    elif AuxnodeTopo.value < removernode.value:
                        AuxnodeTopo.set_dir(removernode.get_dir())
                else:
                    if removernode.value < AuxnodeTopo.value:
                        AuxnodeTopo.set_esq(None)
                    else:
                        AuxnodeTopo.set_dir(None)
            return True

        new_Rbaixo = None  
        node = self.root

        while node and node.value != value:
            new_Rbaixo = node
            if value < node.value:
                node = node.get_esq()
            elif value > node.value:
                node = node.get_dir()


        if node is None or node.value != value:
            return False

        elif node.get_esq() is None and node.get_dir() is None:
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(None)
            else:
                new_Rbaixo.set_dir(None)
            return True

   
        elif node.get_esq() and node.get_dir() is None:
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(node.get_esq())
            else:
                new_Rbaixo.set_dir(node.get_esq())
            return True

        elif node.get_esq() is None and node.get_dir():
            if value < new_Rbaixo.value:
                new_Rbaixo.set_esq(node.get_dir())
            else:
                new_Rbaixo.set_dir(node.get_dir())
            return True
        
        else:
            AuxnodeTopo = node
            removernode = node.get_dir()
            while removernode.get_esq():
                AuxnodeTopo = removernode
                removernode = removernode.get_esq()
            node.value = removernode.value
            if removernode.get_dir():
                if AuxnodeTopo.value > removernode.value:
                    AuxnodeTopo.set_esq(removernode.get_dir())
                elif AuxnodeTopo.value < removernode.value:
                    AuxnodeTopo.set_dir(removernode.get_dir())
            else:
                if removernode.value < AuxnodeTopo.value:
                    AuxnodeTopo.set_esq(None)
                else:
                    AuxnodeTopo.set_dir(None)

        print("Arvore Em-Ordem: ")
        print(self.em_ordem())