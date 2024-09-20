#Código usando dicionários

turma={}
aluno={}

def add_aluno(aluno, matricula, name, age, n1, n2, n3):
    aluno[matricula]={}
    aluno[matricula]['nome']=name
    aluno[matricula]['idade']=age
    aluno[matricula]['nota']={}
    aluno[matricula]['nota']['portugues']=n1
    aluno[matricula]['nota']['matematica']=n2
    aluno[matricula]['nota']['ciencias']=n3
    return aluno

def add_turma(turma, add_t):
    turma[add_t]=[]
    return turma

def alunointurma(aluno, turma, matri, tur):
    if matri in aluno:
        if tur in turma:
            turma[tur].append(aluno[matri])
            return turma
        else:
            print('turma não encontrada')
    else:
        print('matricula não encontrada')

def list_turma(turma, tur):
    if tur in turma:
        print('---alunos presentes na turma:---')
        for cont in turma[tur]:
            print(cont)
    else: 
        print('turma não encontrada')

def boletim(aluno, matri):
    if matri in aluno:
        print('---Aluno:---')
        print(aluno[matri]['nome'])
        m1=int(aluno[matri]['nota']['portugues'])
        m2=int(aluno[matri]['nota']['matematica'])
        m3=int(aluno[matri]['nota']['ciencias'])
        mf=float(((m1+m2+m3)/3))
        print('---Notas do aluno:---')
        print(aluno[matri]['nota'])
        print('---Media do aluno:---')
        print(mf)
    else:
        print('matricula não encontrada')

def relat_turm(turma, tur):
    mf=0
    if tur in turma:
        print('---Alunos presentes na turma:---')
        for cont in turma[tur]:
            print(cont['nome'])
            m1=int(cont['nota']['portugues'])
            m2=int(cont['nota']['matematica'])
            m3=int(cont['nota']['ciencias'])
            mp=float(((m1+m2+m3)/3))
            mf=mf+mp
        media=(mf/len(turma[tur]))
        print('---Media da turma---:')
        print(media)
    else:
        print('turma não encontrada')


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
            matricula = input('informe a matricula do aluno\n')
            name=input('informe o nome do aluno\n')
            age=input('informe a idade do aluno\n')
            n1=input('informe a nota de português do aluno\n')
            n2=input('informe a nota de matematica do aluno\n')
            n3=input('informe a nota de ciencias do aluno\n')
            add_aluno(aluno, matricula, name, age, n1, n2, n3)
            print(aluno)

        elif opc ==2:
            add_t=input('insira o nome da turma que deseja adicionar\n')
            add_turma(turma,add_t)
            print(turma)

        elif opc ==3:
            matri=input('informe a matricula do aluno\n')
            tur=input('informe o nome da turma que o aluno será adicionado\n')
            alunointurma(aluno, turma, matri, tur)
            print(turma)

        elif opc ==4:
            tur=input('informe o nome da turma\n')
            list_turma(turma,tur)
        
        elif opc ==5:
            matri=input('informe o numero da matricula do aluno que deseja receber o boletim\n')
            boletim(aluno, matri)
        
        elif opc ==6:
            tur=input('informe o nome da turma que deseja ver o relatório\n')
            relat_turm(turma, tur)
        elif opc==7:
            break


if __name__ == '__main__':
    main()
