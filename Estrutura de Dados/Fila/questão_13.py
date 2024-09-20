class Fila():
    def __init__(self) -> None:
        self.fila=[]

    def enqueue(self, elemento):
        self.fila.append(elemento)
    
    def mostrar(self):
        print(self.fila)

fila=Fila()
fila_inversa=Fila()
def reverso(fila):
    for n in range(len(fila.fila)):
        cont = -1 - n
        fila_inversa.enqueue(fila.fila[cont])




while True:
    print("1-adicionar elemento a fila")
    print("2-mostrar fila normal")
    print("3-inverter ordem da fila e mostrar")
    print("4-finalizar")
    
    opc=int(input())

    if opc==1:
        elemento = input("insira o nome do elemento\n")
        fila.enqueue(elemento)
    elif opc==2:
        fila.mostrar()
    elif opc==3:
        reverso(fila)
        fila_inversa.mostrar()
    elif opc==4:
        break


    
    