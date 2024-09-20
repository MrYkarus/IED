class Fila():
    def __init__(self) -> None:
        self.fila=[]

    def enqueue(self, elemento):
        self.fila.append(elemento)

    def dequeue(self):
        self.fila.pop(0)
    
    def mostrar_fila(self):
        return self.fila
    
    def is_empty(self):
        if not self.fila:
            return True
        else:
            return False

fila_chamadas=Fila()
fila_atendentes=Fila()

def processar_chamadas(fila_chamadas, fila_atendentes):
    if fila_chamadas.is_empty():
        print("não existem chamadas para serem atendidas")
    elif fila_atendentes.is_empty():
        print("não existem atendentes para chamadas")
    else:
        fila_chamadas.dequeue()
        fila_atendentes.dequeue()

while True:
    print("1-adicionar chamada")
    print("2-adicionar atendente")
    print("3-processar chamadas")
    print("4-mostrar filas")
    print("5-finalizar")
    opc = int(input())

    if opc == 1:
        elemento=input("insira o nome de quem realizará a chamada\n")
        fila_chamadas.enqueue(elemento)

    elif opc == 2:
        elemento=input("insira o nome do atendente\n")
        fila_atendentes.enqueue(elemento)
    
    elif opc == 3:
        processar_chamadas(fila_atendentes, fila_chamadas)
    
    elif opc == 4:
        print("fila de chamadas:")
        print(fila_chamadas.mostrar_fila())
        print("fila de atendentes:")
        print(fila_atendentes.mostrar_fila())

    elif opc == 5:
        break




