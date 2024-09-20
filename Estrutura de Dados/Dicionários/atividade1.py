dici_biblio = {}

def add_livro(dici_biblio, titu, aut, gen):
    dici_biblio[titu]
    dici_biblio[titu]['autor']=aut
    dici_biblio[titu]['genero']=gen
    print('--o livro foi adicionado--')
    return dici_biblio


def remo_livro(livro_desejado):
    if livro_desejado in dici_biblio:
        print('--livro removido--')
        del dici_biblio[livro_desejado]
    else:
        print('o livro não está presente em sua biblioteca')

def busc_livro(dici_biblio, livro_desejado):
    if livro_desejado in dici_biblio:
        print(f'o livro *{livro_desejado}* foi encontrado')
        print ( dici_biblio[livro_desejado] )
    else:
        print('o livro não está presente em sua biblioteca')

def lis_livros(dici_biblio):
    print('Os livros presentes na biblioteca são:')
    for titu in dici_biblio.keys():
        print(titu)
    
def menu():
    print('\n---BEM VINDO(A) A SUA BIBLIOTECA VIRTUAL---')
    print('MENU:')

    print("1-Adicionar um livro a sua biblioteca")
    print("2-Remover um livro da sua biblioteca")
    print("3-Buscar um livro em sua biblioteca")
    print("4-Listar os livros existentes em sua biblioteca")
    print("5- Encerrar sessão")

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)
    

def main():
    while True:
        opc = menu()
        if opc ==1:
            titu = input('informe o titulo:\n')
            aut=input('informe o autor:\n')
            gen=input('informe o genero:\n')
            add_livro(dici_biblio, titu, aut, gen)
        elif opc ==2:
            livro_desejado=input('informe o livro que deseja remover\n')
            remo_livro(livro_desejado)
        elif opc ==3:
            livro_desejado=input('informe o livro que deseja buscar\n')
            busc_livro(dici_biblio, livro_desejado)
        elif opc ==4:
            lis_livros(dici_biblio)
        elif opc ==5:
            break

if __name__ == '__main__':
    main()
