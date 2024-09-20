hotel = []
def add_res(hotel, protocolo, name, quarto, entrada, saida):
    hotelaria ={
        'protocolo': protocolo,
        'nome':name,
        'quarto': quarto,
        'check_in': entrada,
        'check_out': saida
    }

    j=checar(hotel, quarto, entrada, saida)
    if j == 0:
        return hotel
    elif j != 0:
        hotel.append(hotelaria)
        print('reserva adicionada')
        return hotel
    
def data():
    while True:
        dia=int(input('informe o dia:(EX: 1-> dia 1)\n'))
        mes=int(input('informe o mês:(EX:1 -> janeiro)\n'))
        if dia <= 31 and mes <= 12:
            ent=(dia+(mes/100))
            return ent
        elif dia > 31:
            print('dia invalido')
        elif mes > 12:
            print('mes invalido')
            
def checar(hotel,quarto, entrada, saida):
    for i in hotel:
        if i['quarto'] == quarto and i['check_in'] == entrada:
                print('quarto já foi ocupado nesta data')
                return int(0)
        elif i['quarto'] == quarto and i['check_out'] == saida:
                print('quarto já foi ocupado nesta data')
                return int(0)
        
def can_res(res):
    for cont in hotel:
        if cont['protocolo']== res:
            hotel.remove(cont)
            print('---reserva cancelada---')
    print(f'---hotel após cancelamento:---\n {hotel}')
        
    
def busc_res(hotel, res):
    for cont in hotel:
        if cont['protocolo'] == res:
            print (f'---A reserva foi encontrada, veja a seguir:---\n {cont}')
        else:
            print('protocolo inexistente')
            
def lis_res(hotel):
    print('reservas registradas no hotel:')
    for cont in range(len(hotel)):
        print(hotel[cont])
    
def menu_opc():
    print('----MENU DE EDIÇÃO----')
    print('1- Editar nome') 
    print('2- Editar numero do quarto')
    print('3- Editar data de check_in')
    print('4- Editar data de check_out')

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)

def edit_res(hotel, res):
    for cont in hotel:
        if cont['protocolo']==res:
            opc = menu_opc()
            if opc ==1:
                name=input('insira o novo nome:\n')
                cont['nome']= name

            if opc ==2:
                quarto=input('insira o novo numero do quarto:\n')
                cont['quarto']= quarto

            if opc ==3:
                print('-nova data de check_in-\n')
                entrada = (data())
                cont['check_in']= entrada

            if opc ==4:
                print('-nova data de check_out-\n')
                saida= (data())
                cont['check_out']= saida

def menu():
    print('----BEM VINDO(A) AO HOTEL----')
    print('----MENU----')
    print('1- Adicionar reserva') 
    print('2- Cancelar reserva')
    print('3- Buscar reserva')
    print('4- Listar reservas')
    print('5- Editar reserva')
    print('6- Finalizar')

    escolha = input('Informe a opção desejada:\n')
    return int(escolha)

def main():
    protocolo = 0
    while True:
        opc=menu()
        if opc ==1:
            protocolo=protocolo+1
            name=input('informe nome:\n')
            quarto=input('informe o quarto:\n')
            print('-data de check_in-')
            entrada = (data())
            print('-data de check_out-')
            saida= (data())
            add_res(hotel, protocolo, name, quarto, entrada, saida)

        if opc ==2:
            res=int(input('insira o numero do protocolo da reserva que deseja cancelar\n'))
            can_res(res)
            

        if opc ==3:
            res=int(input('insira o numero do protocolo da reserva que deseja buscar\n'))
            busc_res(hotel, res)

        if opc ==4:
            lis_res(hotel)
            
        if opc ==5:
            res=int(input('insira o numero do protocolo da reserva que deseja editar\n'))
            edit_res(hotel, res)
            
        if opc ==6:
            break
           
if __name__ == '__main__':
    main()
