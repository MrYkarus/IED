class Pilha():
    def __init__(self) -> None:
        self.pilha=[]

    def is_empty(self):
        if not self.pilha:
            return True
        else:
            return False
    
    def peek(self):
        if not self.is_empty():
            return self.pilha[-1]
        else:
            return None
        
    def push(self, num):
        self.pilha.append(num)
    
    def pop(self):
        if not self.is_empty():
            return self.pilha.pop()
        else:
            return None

pilha_inicial=Pilha()
pilha_alvo=Pilha()

def validar(pilha_inicial, pilha_alvo):
    cont = 0
    for n in range(len(pilha_alvo.pilha)):
        if pilha_alvo.pilha[n] in pilha_inicial.pilha:
            cont = cont + 1
    if cont == len(pilha_inicial.pilha):
        return True
    else:
        return False

while True:
    print("1-adicionar numero a sequência inicial")
    print("2-adicionar numero a sequência alvo")
    print("3-verificar se a sequencia é valida (OBS: as sequências devem ter o mesmo numero de elemetos)")
    print("4-finalizar")
    opc = int(input())
    
        
    if opc ==1:
        num=input("insira o numero\n")
        pilha_inicial.push(num)

    elif opc ==2:
        num=input("insira o numero\n")
        pilha_alvo.push(num)
    elif opc ==3:
        print(validar(pilha_inicial, pilha_alvo))

    elif opc ==4:
        break
    