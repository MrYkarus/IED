#Código usando dicionário dentro de lista

alunos=[]
turmas=[]

def add_alunos(alunos, matri, name, age, n1, n2, n3):
    al={
        matri:{
            'nome':name,
            'idade':age,
            'notas':{'portugues':n1, 'matematica':n2, 'ciencias': n3}
        }, 
    }
    alunos.append(al)
    return alunos

def add_turmas(turmas, lis):
    tur={
        lis:[]
    }
    turmas.append(tur)
    return turmas

def add_alintur(alunos, turmas, matri, lis):
    for cont in alunos:
        if matri in cont:
            for cont2 in turmas:
                if lis in cont2:
                    cont2[lis].append(cont[matri])
                    print(turmas)

def lis_al(turmas, lis):
    for cont in turmas:
        if lis in cont:
            for cont2 in cont[lis]:
                print(cont2)

def indboletin(alunos, matri):
    mf=0
    for cont in alunos:
        if matri in cont:
            print('---Aluno:---')
            print(cont[matri]['nome'])
            m1=int(cont[matri]['notas']['portugues'])
            m2=int(cont[matri]['notas']['matematica'])
            m3=int(cont[matri]['notas']['ciencias'])
            mf =float(((m1+m2+m3)/3))
            print('---Media---')
            print(mf)

def relturma(turmas, lis):
    mf=0
    for cont in turmas:
        if lis in cont:
            print('---Alunos presentes na turma---')
            for cont2 in cont[lis]:
                print(cont2['nome'])
                m1=int(cont2['notas']['portugues'])
                m2=int(cont2['notas']['matematica'])
                m3=int(cont2['notas']['ciencias'])
                mp =float(((m1+m2+m3)/3))
                mf=mf+mp
            media= mf/(len(cont[lis]))
            print('---Media---')
            print(media)
 
def menu():
    print('\n---Sistema de Turmas, Alunos e Notas---')
    print('MENU:')
    print('1-Adicionar um aluno e suas notas')
    print('2-Adicionar turma')
    print('3-Adicionar aluno em uma turma')
    print('4-Listar os alunos em uma turma')
    print('5-Ver boletim individual do aluno')
    print('6-relatorio de turma')
    print('7-terminar\n')

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)

def main():
    while True:
        opc = menu()
        if opc ==1:
            matri=input('informe a matricula do aluno\n')
            name=input('informe o nome do aluno\n')
            age=input('informe a idade do aluno\n')
            n1=input('informe a nota de português do aluno\n')
            n2=input('informe a nota de matematica do aluno\n')
            n3=input('informe a nota de ciencias do aluno\n')
            add_alunos(alunos,matri, name, age, n1, n2, n3)
            print(alunos)

        elif opc ==2:
            lis=input('informe o nome da turma que deseja adicionar\n')
            add_turmas(turmas, lis)
            print(turmas)

        elif opc ==3:
            lis=input('informe o nome da turma\n')
            matri=input('informe a matricula do aluno\n')
            add_alintur(alunos, turmas, matri, lis)

        elif opc ==4:
            lis=input('infome o nome da turma que deseja ver\n')
            lis_al(turmas, lis)

        
        elif opc ==5:
            matri=input('informe a matricula do aluno\n')
            indboletin(alunos, matri)
        
        elif opc ==6:
            lis=input('informe o nome da turma\n')
            relturma(turmas, lis)
        
        elif opc==7:
            break


if __name__ == '__main__':
    main()