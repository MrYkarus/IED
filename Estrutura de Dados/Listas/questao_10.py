lista1=[]
lista2=[]

def remover_duplicados(lista1, lista2):
    for cont in range(len(lista1)):
        if lista1[cont] != lista1[cont-1]:
            lista2.append(lista1[cont])
    print(lista2)

while True:
    print("1-adicionar item a lista")
    print("2-remover os itens duplicados e mostrar")
    print("3-finalizar")
    opc = int(input())

    if opc == 1:
        print("informe o item")
        item = input()
        lista1.append(item)
    elif opc == 2:
        remover_duplicados(lista1, lista2)
    elif opc == 3:
        break
