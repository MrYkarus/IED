class Pilha():
    def __init__(self) -> None:
        self.pilha=[]
    
    def push(self, elemento):
        self.pilha.append(elemento)

    def pop(self):
        self.pilha.pop(-1)
    
    def peek(self):
        return self.pilha[-1]
    
    def is_empty(self):
        if not self.pilha:
            return True
        else:
            return False
        
pilha=Pilha()
        
def verificação(pilha):
    if pilha.pilha[0]==("(") and pilha.peek() != (")"):
        return False
    elif pilha.pilha[0]==("{") and pilha.peek() != ("}"):
        return False
    elif pilha.pilha[0]==("[") and pilha.peek() != ("]"):
        return False
    else:
        return True

while True:
    print("1-adicionar elemento")
    print("2-verificação")
    print("3-finalizar")
    opc = int(input())
    if opc ==1:
        print("adicione um elemento da expressão")
        elemento = input()
        pilha.push(elemento)

    elif opc ==2:
        print(verificação(pilha))

    elif opc ==3:
        break
