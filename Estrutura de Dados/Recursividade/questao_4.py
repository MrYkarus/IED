lista_recursiva=[]

def soma(lista_recursiva):
    if len(lista_recursiva) == 1:
        return lista_recursiva[0]
    else:
        return lista_recursiva[0] + soma(lista_recursiva[1:])
    
while True:    
    print("1-adicionar numero a lista")
    print("2-somar e mostrar a soma dos itens da lista")
    print("3-finalizar")
    opc =int(input())

    if opc ==1:
        print("informe um numero da lista")
        n = int(input())
        lista_recursiva.append(n)

    if opc ==2:
        print(soma(lista_recursiva))

    if opc ==3:
        break