class Fila():
    def __init__(self):
        self.fila=[]
    
    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        self.fila.pop(0)

    def is_empty(self):
        if not self.fila:
            return True
        else:
            return False
    def mostrar(self):
        return self.fila
        
    def front(self):
        return self.fila[0]
    def esvaziar(self):
        for i in range(len(self.fila)):
            self.fila.pop()

class Pilha():
    def __init__(self):
        self.pilha=[]

    def push(self, item):
        self.pilha.append(item)

    def excluir(self, item):
        self.pilha.remove(item)

    def is_empty(self):
        if not self.pilha:
            return True
        else:
            return False
    def base(self):
        return self.pilha[0]
    def processo(self):
        self.pilha.pop(0)
    

pilha_urgente= Pilha()
pilha_normal= Pilha()
fila_principal= Fila()

def adicionar(item, nivel):
    if nivel==1:
        pilha_urgente.push(item)
    elif nivel==2:
        pilha_normal.push(item)
    else:
        print("opção inválida")

def processar(pilha_urgente, pilha_normal):
    for n in range(len(pilha_urgente.pilha)):
            fila_principal.enqueue(pilha_urgente.pilha[n])
    for n in range(len(pilha_normal.pilha)):
            fila_principal.enqueue(pilha_normal.pilha[n])

    return fila_principal.mostrar()

def remover(item, nivel):
    if nivel==1:
        pilha_urgente.excluir(item)
    elif nivel==2:
        pilha_normal.excluir(item)

while True:
    print("1-adicionar solicitação")
    print("2-atender solicitação")
    print("3- remover solicitação")
    print("4-consultar proxima solicitação")
    print("5-finalizar")
    opc =int(input())

    if opc == 1:
        print("informe a solicitação")
        item=input()
        print("informe o nivel de urgência")
        print("1-urgente || 2-normal")
        nivel=int(input())
        adicionar(item, nivel)

    if opc ==2:
        print("fila antes do atendimento:")
        print(processar(pilha_urgente, pilha_normal))
        fila_principal.esvaziar()
        print("fila após processamento")
        if pilha_urgente.is_empty():
            pilha_normal.processo()
        else: 
            pilha_urgente.processo()
        print(processar(pilha_urgente, pilha_normal))
        fila_principal.esvaziar()


    
    if opc ==3:
        print("informe a solicitação que deseja remover")
        item=input()
        print("informe a prioridade dessa solicitação")
        print("1-urgente || 2-normal")
        nivel=int(input())
        remover(item, nivel)
    
    if opc ==4:
        if pilha_urgente.is_empty():
            print("o próximo item da fila a ser processado é:")
            print(pilha_normal.base())
        else:
            print("o próximo item da fila a ser processado é:")
            print(pilha_urgente.base())
    
    if opc ==5:
        break
        
       
    
