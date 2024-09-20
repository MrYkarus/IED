class Fila:
    def __init__(self) -> None:
        self.fila=[]

    def enqueue(self, cliente):
        self.fila.append(cliente)
    
    def dequeue(self):
        self.fila.pop(0)

    def front(self):
        return self.fila
    
    def is_empty(self):
        if not self.fila:
            return True
        else:
            return False
        
fila = Fila()
def adicionar(fila, cliente):
    fila.enqueue(cliente)
    print("cliente adicionado\n")

def atender(fila):
    fila.dequeue()
    print("cliente atendido\n")

def mostrar_fila(fila):
    print(fila.front())

while True:
    print("1-adicionar cliente a fila")
    print("2-atender cliente")
    print("3-mostrar fila")
    print("4-finalizar")
    opc = int(input())

    if opc ==1:
        cliente = input("informe o nome do cliente\n")
        adicionar(fila, cliente)
        
    if opc ==2:
        atender(fila)
    if opc ==3:
        mostrar_fila(fila)
    if opc ==4:
        break
