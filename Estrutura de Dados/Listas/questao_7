lista=[]
def adicionar(lista, item):
    lista.append(item)
def remover(lista, item):
    if item in lista:
        lista.remove(item)
    else:
        print("o item não foi encontrado\n")
def busca(lista, item):
    if item in lista:
        print("o item está na lista\n")
    else:
        print("o item não está na lista\n")

while True:
    print("1- adicionar item")
    print("2- remover item")
    print("3- buscar item")
    print("4- ver lista")
    print("5- finalizar")
    opc=int(input(""))

    if opc == 1:
        item = input("informe o item que deseja adicionar \n")
        adicionar(lista, item)
    elif opc == 2:
        item = input("informe o item que deseja remover \n")
        remover(lista, item)
    elif opc == 3:
        item = input("informe o item que deseja buscar \n")
        busca(lista, item)
    elif opc == 4:
        for cont in range(len(lista)):
            print(lista[cont])
    else:
        break
