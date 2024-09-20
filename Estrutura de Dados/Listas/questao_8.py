lista=[]
lista_reversa=[]

def reversão(lista):
    for cont in range(len(lista)):
        n = -1 - cont
        lista_reversa.append(lista[n])
    print(lista_reversa)

while True:
    print("1-adicionar item")
    print("2-reverter ordem e mostrar lista")
    print("3-finalizar")
    opc = int(input())

    if opc == 1:
        print("informe o item que deseja adicionar")
        item = input()
        lista.append(item)
    elif opc ==2:
        reversão(lista)

    elif opc == 3:
        break
