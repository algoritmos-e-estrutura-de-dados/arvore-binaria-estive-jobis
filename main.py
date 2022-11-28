from binary_tree import BinaryTree

binary_tree = BinaryTree()

while (True):
    print("1) entrar com um novo valor") 
    print("2) print Pré-ordem") 
    print("3) print Em-ordem") 
    print("4) print Pós-ordem") 
    print("5) buscar") 
    print("6) Remover") 
    print("7) Sair ") 
    operacao = input()

    if (operacao == "1"):
        value = input("Escreva o valor: ")
        binary_tree.adicionar(int(value))

    elif (operacao == "2"):
        print("Pré-Ordem: ")
        binary_tree.pre_ordem()
        pass

    elif (operacao == "3"):
        print("Em Ordem: ")
        binary_tree.em_ordem()
        pass    
    elif (operacao == "4"):
        print("Pos-Ordem: ")
        binary_tree.pos_ordem()
        pass

    elif (operacao == "5"):
        value = int(input("Entre com o valor que ser consultado"))
        print("Valor foi encontrado" if binary_tree.procurar(value) else "Valor não foi encontrado")
        pass

    elif (operacao == "6"):
        value = int(input("Entre com o valor que deseja a ser removido: "))
        print("Valor removido" if binary_tree.remover(value) else "Valor não removido, innexistente")

        print("Arvore atualizada Pré-Ordem: ")
        binary_tree.pre_ordem()
        print("Arvore atualizada Em-Ordem: ")
        binary_tree.em_ordem()
        print("Arvore atualizada Pós-Ordem: ")
        binary_tree.pos_ordem()
        pass

    elif (operacao == "7"):
        print("Fim")
        break

    else:
        print("Opção Invalida")
        pass