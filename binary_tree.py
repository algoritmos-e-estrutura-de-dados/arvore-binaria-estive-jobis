from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def adicionar(self, value):
        if value < self.value:
            if self.esquerda is None:
                    self.esquerda = Node(value)
            else:
                self.esquerda.adicionar(value)
        else: 
            if self.direita is None: 
                self.right = Node(value)
            else: 
                self.direita.adicionar(value)
                
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

    # Método Remover
    def remover(root, key):
        if not root:
            return root

        if root.val > key:
            root.esquerda = remover(root.esquerda, key)

        elif root.val < key:
            root.direita = remover(root.direita, key)

        else:
            
            if not root.direita:
                return root.esquerda

            if not root.esquerda:
                return root.direita
  
            temp_value = root.direita
            mini_value = temp_value.value
            while temp_value.esquerda:
                temp_value = temp_value.esquerda
                mini_value = temp_value.value
                
            root.direita = remover(root.direita, root.value)
        return root
    
    def Altura(root):
        if root is None:
            return 0
        return max(Altura(root.esquerda), Altura(root.direita))+1
    
    def getcol(h):
        if h == 1:
            return 1
        return getcol(h-1) + getcol(h-1) + 1

    def printArvore(M, root, col, Coluna, Altura):
        if root is None:
            return
        M[row][col] = root.data
        printArvore(M, root.esquerda, col-pow(2, Altura-2), Coluna+1, Altura-1)
        printArvore(M, root.direita, col+pow(2, Altura-2), Coluna+1, Altura-1)

    def PrinterDaArvore():
        h = altura(Arvore.root)
        col = getcol(h)
        M = [[0 for _ in range(col)] for __ in range(h)]
        printArvre(M, Arvore.root, col//2, 0, h)
        for i in M:
            for j in i:
                if j == 0:
                    print(" ", end=" ")
                else:
                    print(j, end=" ")
            print("")
    