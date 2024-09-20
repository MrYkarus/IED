class Aluno:
    def __init__(self, name, n1, n2):
        self.name=name
        self.n1=n1
        self.n2=n2
        
    def al(self):
        self.aluno={
            'nome':self.name,
            'n1': self.n1,
            'n2':self.n2
        }
        return self.aluno
    
class Turma:
    def __init__(self):
        self.alunos=[]
    
    def criar_tur(self,esc):
        self.alunos.append(esc)
        return self.alunos
    
    def delet_tur(self,esc):
        for cont in self.alunos:
            if esc == cont['nome']:
                self.alunos.remove(cont)
                return self.alunos

    def listar(self):
        for cont in self.alunos:
            print(cont)
    
    def edit(self, esc, opc2):
        for cont in self.alunos:
            if esc == cont['nome']:
                if opc2==1:
                    name=input('insira o novo nome:\n')
                    cont['nome']= name
                elif opc2==2:
                    n1=int(input('insira a nova nota da n1:\n'))
                    cont['n1']= n1
                elif opc2==3:
                    n2=int(input('insira a nova nota da n2:\n'))
                    cont['n2']= n2
                           
    def media(self,esc):
        for cont in self.alunos:
            if esc == cont['nome']:
                n1=cont['n1']
                n2=cont['n2']
                media=float(((n1*2)+(n2*3))/5)
                return media  
            
def situ(media):  
    if media >= 7:
        print('||Aluno acima da media||\n') 
    else:
        print('||Aluno abaixo da media||\n')
        
def menu_edit():
    print('1-editar nome')
    print('2-editar a nota da n1')
    print('3-editar a nota da n2')
    escolha=int(input('\ninforme a opção desejada\n'))
    return escolha           

def menu():
    print('\n=== MENU ===')
    print('1-adicionar aluno a turma')
    print('2-excluir aluno da turma')
    print('3-listar alunos na turma')
    print('4-editar aluno na turma')
    print('5-ver media do aluno e sua situação')
    print('6-fim')
    escolha=int(input('\ninforme a opção desejada\n'))
    return escolha

turmas= Turma()

def main():
    while True:
        opc=menu()
        if opc==1:
            name=input('informe o nome do aluno\n')
            n1=int(input('informe a n1\n'))
            n2=int(input('informe a n2\n'))
            aluno=Aluno(name, n1, n2)
            esc=aluno.al()
            turmas.criar_tur(esc)
            print('|| aluno adicionado ||\n')
            
        elif opc==2:
            esc=input('informe o nome do aluno que deseja excluir da turma\n')
            turmas.delet_tur(esc)
            print('|| aluno removido ||\n')
        
        elif opc ==3:
            print('|| alunos pesentes na turma ||')
            turmas.listar()
        
        elif opc ==4:
            esc=input('informe o nome do aluno que deseja editar as informações\n')
            opc2=menu_edit()
            turmas.edit(esc, opc2)
        
        elif opc ==5:
            esc=input('informe o nome do aluno que deseja ver a media e a situação\n')
            media=(turmas.media(esc))
            print(f'||Media Ponderada do aluno: {media}||')
            situ(media)   
        
        elif opc ==6:
            break
            
if __name__ == "__main__":
    main()
