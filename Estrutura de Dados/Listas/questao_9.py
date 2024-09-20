lista1=[]
lista2=[]

def intercalar_listas(lista1, lista2):
    for cont in range(len(lista2)):
        lista1.append(lista2[cont])
    print(lista1)

while True:
    print("1-adicionar item na lista 1")
    print("2-adicionar item na lista 2")
    print("3-juntar as listas e mostrar")
    print("4-finalizar")
    opc = int(input())

    if opc == 1:
        print("informe o item")
        item = input()
        lista1.append(item)
    elif opc == 2:
        print("informe o item")
        item = input()
        lista2.append(item)
    elif opc == 3:
        intercalar_listas(lista1, lista2)
    elif opc == 4:
        break