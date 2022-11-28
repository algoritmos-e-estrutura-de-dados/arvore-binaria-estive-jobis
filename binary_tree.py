from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            auxiliar = self.root
            while (True):
                if (auxiliar.value >= value):
                    ref_cima = auxiliar
                    auxiliar = auxiliar.getEsquerda()
                    ref_baixo = True

                else:
                    ref_cima = auxiliar
                    auxiliar = auxiliar.getDireita()
                    ref_baixo = False

                if (auxiliar is None):
                    break
                if ref_baixo is False:
                    ref_cima.set_dir(node)
                else:
                    ref_cima.set_esq(node)

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

                aux_node_ref_topo = self.root      
                remove_node: Node = self.root.get_dir()     #

                while (remove_node.get_esq()):
                    aux_node_ref_topo = remove_node
                    remove_node = remove_node.get_esq()

                self.root.value = remove_node.value
                if remove_node.get_dir():
                    if aux_node_ref_topo.value > remove_node.value:
                        aux_node_ref_topo.set_esq(remove_node.get_dir())
                    elif aux_node_ref_topo.value < remove_node.value:
                        aux_node_ref_topo.set_dir(remove_node.get_dir())
                else:
                    if remove_node.value < aux_node_ref_topo.value:
                        aux_node_ref_topo.set_esq(None)
                    else:
                        aux_node_ref_topo.set_dir(None)
            return True

        new_ref_baixo = None  
        node = self.root

        while node and node.value != value:
            new_ref_baixo = node
            if value < node.value:
                node = node.get_esq()
            elif value > node.value:
                node = node.get_dir()


        if node is None or node.value != value:
            return False

        elif node.get_esq() is None and node.get_dir() is None:
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(None)
            else:
                new_ref_baixo.set_dir(None)
            return True

   
        elif node.get_esq() and node.get_dir() is None:
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(node.get_esq())
            else:
                new_ref_baixo.set_dir(node.get_esq())
            return True

        elif node.get_esq() is None and node.get_dir():
            if value < new_ref_baixo.value:
                new_ref_baixo.set_esq(node.get_dir())
            else:
                new_ref_baixo.set_dir(node.get_dir())
            return True
        
        else:
            aux_node_ref_topo = node
            remove_node = node.get_dir()
            while remove_node.get_esq():
                aux_node_ref_topo = remove_node
                remove_node = remove_node.get_esq()
            node.value = remove_node.value
            if remove_node.get_dir():
                if aux_node_ref_topo.value > remove_node.value:
                    aux_node_ref_topo.set_esq(remove_node.get_dir())
                elif aux_node_ref_topo.value < remove_node.value:
                    aux_node_ref_topo.set_dir(remove_node.get_dir())
            else:
                if remove_node.value < aux_node_ref_topo.value:
                    aux_node_ref_topo.set_esq(None)
                else:
                    aux_node_ref_topo.set_dir(None)

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
        print("Arvore atualizada (Pré-Ordem): ")
        print(self.pre_ordem())
        print("Arvore atualizada (Em-Ordem): ")
        print(self.em_ordem())
        print("Arvore atualizada (Pós-Ordem): ")
        print(self.pos_ordem())