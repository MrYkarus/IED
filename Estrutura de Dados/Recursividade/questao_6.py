elementos = []
def subconjuntos(elementos, n = 0, conjunto = []):
    if n == len(elementos):
        print(conjunto)
    else:
        subconjuntos(elementos, n + 1, conjunto + [elementos[n]])
        subconjuntos(elementos, n + 1, conjunto)

numero_elementos = int(input("Informe o numero de elementos do seu conjunto: "))  
cont = 0
while cont < numero_elementos:
    elementos.append(input(f'Digite o elemento {cont + 1}: '))
    cont += 1

subconjuntos(elementos)