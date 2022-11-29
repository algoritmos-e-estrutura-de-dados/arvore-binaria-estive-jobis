from binary_tree import BinaryTree

binary_tree = BinaryTree()

while (True):
    print("1) entrar com um novo valor") 
    print("2) printar") 
    print("3) buscar") 
    print("4) Remover") 
    print("5) Sair ") 
    operacao = input()

    if (operacao == "1"):
        value = input("Escreva o valor: ")
        binary_tree.adicionar(int(value))

    elif (operacao == "2"):
        print("Em Ordem: ")
        node.Print()
        pass    

    elif (operacao == "3"):
        value = int(input("Entre com o valor que ser consultado"))
        print("Valor foi encontrado" if binary_tree.procurar(value) else "Valor não foi encontrado")
        pass

    elif (operacao == "4"):
        value = int(input("Entre com o valor que deseja a ser removido: "))
        print("Valor removido" if binary_tree.remover(value) else "Valor não removido, innexistente")

    elif (operacao == "5"):
        print("Fim")
        break

    
    else:
       print("Opção Invalida")
pass