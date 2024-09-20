g_estoque = []

def add_prod(g_estoque, cod, name, quant, pre):
    estoque ={
        'codigo': cod,
        'name': name,
        'quantidade':quant,
        'preço': pre
    }
    g_estoque.append(estoque)
    print('produto adicionado')
    print(g_estoque)
    return g_estoque 

def exc_prod(des):
    for cont in g_estoque:
        if cont['codigo']==des:
            g_estoque.remove(cont)
            print('---reserva cancelada---')
    print(f'---estoque apos cancelamento:---\n {g_estoque}')

def atualizar(g_estoque, des):
    for cont in g_estoque:
        if cont['codigo']==des:
            opc = menu_opc()

            if opc ==1:
                name = input('informe o novo nome\n')
                cont['name']=name

            elif opc ==2:
                quant=input('informe a nova quantidade do produto\n')
                cont['quantidade']=quant

            elif opc ==3:
                pre=input('informe o novo preço do produto\n')
                cont['preço']=pre

def lis_prod(g_estoque):
    print('produtos registrados no estoque:')
    for cont in range(len(g_estoque)):
        print(g_estoque[cont])

def busc_prod(g_estoque, des):
    for cont in g_estoque:
        if cont['codigo'] == des:
            print (f'---A reserva foi encontrada, veja a seguir:---\n {cont}')
        else:
            print('protocolo inexistente')

def filt_estoque(g_estoque, filt):
    if filt==1:
        filt_quantidade=input('insira a quantidade maxima para os produtos que deseja ver\n')
        for cont in g_estoque:
            if cont['quantidade'] <= filt_quantidade:
                print(cont['name'])
    elif filt==2:
        filt_preco=input('insira o preço maximo para os produtos que deseja ver\n')
        for cont in g_estoque:
            if cont['preço'] <= filt_preco:
                print(cont['name'])

def relatorio(g_estoque):
    res=0
    for cont in g_estoque:
        rel_quant= int(cont['quantidade'])
        rel_pre= float(cont['preço'])
        res = res + (rel_quant*rel_pre)
    print(f'o preço total do estoque é igual a:\n{res}')
                

def menu_opc():
    print('----MENU DE EDIÇÃO----')
    print('1- Editar nome') 
    print('2- Editar quantidade do produto')
    print('3- Editar preço do produto')

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)

def menu():
    print('----SISTEMA DE ESTOQUE----')
    print('----MENU----')
    print('1-Adicionar produto') 
    print('2-Remover produto')
    print('3-Atualizar estoque ')
    print('4-Visualizar estoque')
    print('5-buscar produto por codigo')
    print('6-Filtrar produtos')
    print('7-Gerar relatorio ')
    print('8-Finalizar')

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)

def main():
    cod=0
    while True:
        opc=menu()

        if opc==1:
            cod = cod+1
            name= input('informe o nome do produto\n')
            quant=input('informe a quantidade do produto\n')
            pre=input('informe o preço do produto\n')
            add_prod(g_estoque, cod, name, quant, pre)
        
        elif opc==2: 
            des=int(input('informe o codigo do produto que deseja excluir\n'))
            exc_prod(des)
        
        elif opc==3:
            des=int(input('informe o codigo do produto que deseja atualizar as informações\n'))
            atualizar(g_estoque, des)
        
        elif opc==4:
            lis_prod(g_estoque)
        
        elif opc==5:
            des= int(input('informe o codigo do produto que deseja buscar'))
            busc_prod(g_estoque, des)
        
        elif opc==6:
            print('informe o filtro desejado')
            print('1-quantidade\n2-preço')
            filt=int(input(''))
            filt_estoque(g_estoque, filt)
        
        elif opc ==7:
            relatorio(g_estoque)
        
        elif opc==8:
            break

if __name__ == '__main__':
    main()