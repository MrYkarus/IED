class Biblioteca:
    def __init__(self):
        self.bibli=[]
        self.regis=[]
        
    def cad_liv(self, livrobusc):
        self.bibli.append(livrobusc)
    
    def mostrar_registro(self):
        for cont in self.regis:
            print (cont)

    
    def disp(self, name):
        for cont in self.bibli:
            if cont['titulo'] == name:
                if cont['disponibilidade']==True:
                    cont['disponibilidade']=False
                    print('---livro reservado---\n')
                    self.regis.append(cont['titulo'])
                else:
                    print('o livro não esta mais disponivel')
            else:
                print('livro não encontrado')

    def in_disp(self, name):
        for cont in self.bibli:
            if cont['titulo'] == name:
                if cont['disponibilidade']==False:
                    cont['disponibilidade']=True
                    print('---livro devolvido---\n')
                    self.regis.remove(cont['titulo'])
                else:
                    print('o livro não foi reservado')
            else:
                print('livro não encontrado')


class Livros:
    def __init__(self, titu, aut, ano):
        self.titu=titu
        self.aut=aut
        self.ano=ano
    
    def add_livro(self):
        self.liv={
            'titulo':self.titu,
            'autor':self.aut,
            'publicação':self.ano,
            'disponibilidade':True
        }
        return self.liv

biblioteca=Biblioteca()
    
def menu():
        print('||======== Biblioteca =========||')
        print('|| 1 - Adicionar livro         ||')
        print('|| 2 - Emprestar ou Devolver   ||')
        print('|| 3 - Registro de Emprestimos ||')
        print('|| 4 - Fechar                  ||')
        print('||=============================||')

        escolha=int(input('\ninforme a opção desejada\n'))
        return escolha
def menu_emprestimo():
        print('||==EMPRESTIMO//DEVOLUÇÃO==||')
        print('|| 1 - EMPRESTIMO          ||')
        print('|| 2 - DEVOLUÇÃO           ||')
        print('||=========================||')

        escolha=int(input('\ninforme a opção desejada\n'))
        return escolha
    
def main():
    while True:
        opc=menu()
        if opc ==1:
            titu=str(input("||Informe o nome do livro||\n"))
            aut=str(input("||Informe o autor do livro||\n"))
            ano=int(input("||Informe o ano de publicação do livro||\n"))
            livro=Livros(titu, aut, ano)
            livrobusc=livro.add_livro()
            biblioteca.cad_liv(livrobusc)
            print('---livro adicionado a biblioteca---\n')
        
        elif opc ==2:
            opc2=menu_emprestimo()
            if opc2==1:
                name=input('||informe o nome do livro que deseja pegar emprestado||')
                biblioteca.disp(name)
                

            elif opc2==2:
                name=input('||informe o nome do livro que deseja devolver||')
                biblioteca.in_disp(name)
                
        
        elif opc ==3:
            print('--- REGISTRO DE LIVROS RESERVADOS ---')
            biblioteca.mostrar_registro()
        
        elif opc ==4:
            break


if __name__ == "__main__":
    main()