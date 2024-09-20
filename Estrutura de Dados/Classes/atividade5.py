class Calc:
    def __init__(self, s1, s2):
        self.s1=s1
        self.s2=s2

    def som(self):
        result = self.s1+self.s2
        return result

    def sub(self):
        result = self.s1-self.s2
        return result

    def mult(self):
        result = self.s1*self.s2
        return result

    def div(self):
        result = self.s1/self.s2
        return result

def pedir_num():
    n1=int(input('informe o primeiro numero\n'))
    n2=int(input('informe o segundo numero\n'))
    return n1, n2
def menu():

    print('====== Menu ========')
    print('== 1-somar        ==')
    print('== 2-subtrair     ==')
    print('== 3-multipilcar  ==')
    print('== 4-dividir      ==')
    print('====================')

    escolha=int(input('\ninforme a opção desejada\n'))
    return escolha

def main():
    while True:
        opc=menu()
        if opc==1:
            s1, s2=(pedir_num())
            calc = Calc(s1, s2)
            print('\n===RESULTADO DA SOMA===\n')
            print(calc.som())

        elif opc ==2:
            s1, s2=(pedir_num())
            calc = Calc(s1, s2)
            print('\n===RESULTADO DA SUBTRAÇÃO===\n')
            print(calc.sub())
        
        elif opc ==3:
            s1, s2=(pedir_num())
            calc = Calc(s1, s2)
            print('\n===RESULTADO DA MULTIPLICAÇÃO===\n')
            print(calc.mult())
        
        elif opc ==4:
            s1, s2=(pedir_num())
            if s2 != 0:
                calc = Calc(s1, s2)
                print('\n===RESULTADO DA DIVISÃO===\n')
                print(calc.div())
            else:
                print('nenhum numero pode ser dividido por 0')
            

            
if __name__ == "__main__":
    main()
