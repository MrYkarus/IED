class Pilha():
    def __init__(self) -> None:
        self.pilha=[]

    def is_empty(self):
        if not self.pilha:
            return True 
        else:
            return False
    
    def push(self, numero):
        self.pilha.append(numero)
    
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

    
pilha = Pilha()

def bin(numero):
    while numero > 0:
        binario = numero % 2
        pilha.push(binario)
        numero = numero // 2
    string = ""
    for cont in range(len(pilha.pilha)):
        n= -1 - cont
        string = string + str(pilha.pilha[n])
    return string

while True:
    print("1-adicionar numero e mostrar em binario")
    print("2-finalizar")
    opc = int(input())
    if opc ==1:
        numero=int(input("informe o numero\n"))
        print(bin(numero))
    elif opc ==2:
        break
