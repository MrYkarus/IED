
class Fila():
    def __init__(self):
        self.fila = []

    def is_empty(self):

        if not self.fila:
            return True
        else:
            return False


    def enqueue(self, item):
        self.fila.append(item)


    def dequeue(self):
            self.fila.pop(0)

    
    def mostrar(self):
        return self.fila
    


    
    
    


fila_alta = []
fila_media = []
fila_baixa = []
fila_processo = Fila()



def alta(item):
    fila_alta.append(item)
    return fila_alta

def media(item):
    fila_media.append(item)
    return fila_media

def baixa(item):
    fila_baixa.append(item)
    return fila_baixa


def processar_tarefa(fila_alta):
    for n in range(len(fila_alta)):
            fila_processo.enqueue(fila_alta[n])
    print("fila antes do processamento:")
    print(fila_processo.mostrar())
    fila_processo.dequeue()
    print("fila depois do processamento:")
    print(fila_processo.mostrar())



while True:
    print("1-adicionar tarefa")
    print("2-remover tarefa")
    print("3-processar tarefa mostrando antes e depois e finalizar")
    opc = int(input())

    if opc ==1:
        print("informe a tarefa")
        item = input()
        print('Defina a prioridade da tarefa: ')
        print('1 - alta || 2 - Média || 3 - baixa')
        prioridade= int(input())
        if prioridade ==1:
            alta(item)
        if prioridade ==2:
            media(item)
        if prioridade==3:
            baixa(item)
        
    elif opc ==2:
        print("qual a prioridade do item que deseja remover?")
        print('1 - alta || 2 - Média || 3 - baixa')
        pri=int(input())
        if pri ==1:
            print("informe o item que deseja remover")
            remover = input()
            fila_alta.remove(remover)
        if pri ==2:
            print("informe o item que deseja remover")
            remover = input()
            fila_media.remove(remover)
        if pri ==3:
            print("informe o item que deseja remover")
            remover = input()
            fila_baixa.remove(remover)



    elif opc ==3:
        fila_alta.extend(fila_media)
        fila_alta.extend(fila_baixa)
        processar_tarefa(fila_alta)
        break
        




