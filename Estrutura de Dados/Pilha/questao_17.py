class Pilha():
    def __init__(self) -> None:
        self.pilha=[]

    def is_empty(self):
        if not self.fila:
            return True
        else:
            return False
        
    def push(self, num):
        self.pilha.append(num)

    def pop(self):
        if not self.is_empty():
            return self.pilha.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.pilha[-1]
        else:
            return None
    
    def min(self):
        menor = self.pilha[0]
        for n in range(len(self.pilha)):
            if menor > self.pilha[n]:
                menor = self.pilha[n]
        return menor

pilha=Pilha()
while True:
    print("1-adicionar numero")
    print("2-mostrar menor valor")
    print("3-finalizar")
    opc = int(input())
    if opc ==1:
        num=int(input("informe o numero\n"))
        pilha.push(num)
    elif opc ==2:
        print(pilha.min())

    elif opc ==3:
        break
         