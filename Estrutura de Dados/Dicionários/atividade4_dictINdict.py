#Código usando dicionários dentro de dicionários

alunos={}
turmas={}

def addal(alunos, matricula, name, age,n1,n2,n3 ):
    aluno={
        'nome':name,
        'idade':age,
        'notas':{'portugues':n1, 'matematica':n2, 'ciencias':n3}
    }

    alunos[matricula]=aluno
    return alunos


def addtur(turmas, addtu):
    turmas[addtu]=[]
    return turmas
    
def alintur(turmas, alunos, tu,matri):
    if tu in turmas and matri in alunos:
        turmas[tu].append(alunos[matri])
    
def lisalintur(turmas, tu):
    if tu in turmas:
        print('---Alunos presentes na turma---')
        for cont in turmas[tu]:
            print(cont)

    
def medal(alunos):
    mf=0
    print('---Nome dos alunos---')
    for cont in alunos:
        m1=int(alunos[cont]['notas']['portugues'])
        m2=int(alunos[cont]['notas']['matematica'])
        m3=int(alunos[cont]['notas']['ciencias'])
        mp=((m1+m2+m3)/3)
        mf= mf+mp
        print(alunos[cont]['nome'])
    media=mf/len(alunos)
    print(f'---Media dos alunos---\n{media}')
    

def medtur(turmas):
    mf=0
    co=0
    print('---Nome dos alunos presentes nas turmas---')
    for cont in turmas:
        for cont2 in turmas[cont]:
            co=co+1
            m1=int(cont2['notas']['portugues'])
            m2=int(cont2['notas']['matematica'])
            m3=int(cont2['notas']['ciencias'])
            mp=((m1+m2+m3)/3)
            mf= mf+mp
            print(cont2['nome'])
    media=(mf/co)
    print(f'---Media das turmas---\n{media}')

def boletim(alunos,matri):
        if matri in alunos:
            m1=int(alunos[matri]['notas']['portugues'])
            m2=int(alunos[matri]['notas']['matematica'])
            m3=int(alunos[matri]['notas']['ciencias'])
            mf=float(((m1+m2+m3)/3))
            print(f'---Nome do aluno---')
            print(alunos[matri]['nome'])
            print('---Notas do Aluno---')
            print(alunos[matri]['notas'])
            print(f'---Media do aluno:---\n{mf}')

def indturmed(turmas, tu):
    if tu in turmas:
        mf=0
        print(f'---Alunos presentes na turma: {tu}')
        for cont in turmas[tu]:
            m1=int(cont['notas']['portugues'])
            m2=int(cont['notas']['matematica'])
            m3=int(cont['notas']['ciencias'])
            mp=((m1+m2+m3)/3)
            mf= mf+mp
            print(cont['nome'])
    media=mf/len(turmas[tu])
    print(f'---Media da turma---\n{media}')

def menu():
    print('1-adicionar aluno')
    print('2-adicionar turma')
    print('3-adicionar aluno na turma')
    print('4-listar alunos na turma')
    print('5-media dos alunos')
    print('6-media das turmas')
    print('7-boletim individual')
    print('8-media de uma turma')
    print('9-fim')

    selecionar=input('opc desejada:\n')
    return int(selecionar)
def main():
    matricula=0
    while True:
        opc = menu()
        if opc ==1:
            matricula=matricula+1
            name=input('nome do aluno para add:\n')
            age=input('idade do aluno para add:\n')
            n1=int(input('nota portugues:\n'))
            n2=int(input('nota matematica:\n'))
            n3=int(input('nota ciencias:\n'))
            addal(alunos, matricula, name, age,n1,n2,n3 )
            print(alunos)
        
        elif opc ==2:
            addtu=input('nome da turma para add\n')
            addtur(turmas, addtu)
            print (turmas)
        
        elif opc ==3:
            tu=input('informe o nome da turma que vai receber\n')
            matri= int(input('informe a matricula do aluno que vai ser adicionado\n'))
            alintur(turmas, alunos, tu,matri)
            print (turmas)

        elif opc ==4:
            tu=input('informe o nome da turma que vai ser listada:\n')
            lisalintur(turmas, tu)
        
        elif opc ==5:
            medal(alunos)

        elif opc ==6:
            medtur(turmas)
        
        elif opc ==7:
            matri=int(input('informe a matricula do aluno\n'))
            boletim(alunos,matri)

        elif opc ==8:
            tu=input('informe o nome da turma\n')
            indturmed(turmas, tu)
        
        elif opc ==9:
            break

if __name__=='__main__':
    main()