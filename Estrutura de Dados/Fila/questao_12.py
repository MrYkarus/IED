class Fila():
    def __init__(self) -> None:
        self.fila=[]

    def enqueue(self, pessoa):
        self.fila.append(pessoa)

    def passar_final(self, n):
        for cont in range(n):
            self.fila.append(self.fila[0])
            self.fila.pop(0)
        print (self.fila)
    
fila=Fila()

while True:
    print("1-adicionar pessoa a fila")
    print("2-passar pessoa da frente para o fim da fila e mostrar\n")
    print("3-finalizar")
    opc=int(input())

    if opc==1:
        pessoa = input("insira o nome da pessoa")
        fila.enqueue(pessoa)
    elif opc==2:
        n = int(input("informe o numero de vezes que a operação deve ser feita\n"))
        fila.passar_final(n)
    elif opc==3:
        break
