def permuta(string):
    lista=[]
    if len(string) <= 1:
        return string
    else:
        for n in range(len(string)):
            auxiliar = string[:n] + string[n+1:]
            for i in permuta(auxiliar):
                lista.append(string[n] + i)
        return lista

print("informe a string")
string = input()
print(permuta(string))