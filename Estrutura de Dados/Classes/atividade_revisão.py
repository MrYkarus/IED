class Livro:
    def __init__(self,titu,aut,quant,pre):
        self.titu=titu
        self.aut=aut
        self.quant=quant
        self.pre=pre
    
    def add_stock(self, esc):
        if esc >= 0:
            self.quant=esc
        else:
            print('O valor da quantidade deve ser positiva')
    
    def sell_stock(self, item):
        if item>0:
            if item<=self.quant:  
                new = self.quant-item
                self.quant=new
            else:
                print('o numero para compra deve ser menor ou igual ao numero do estoque')
        else:
            print('o numero de compra deve ser maior que 0')

    def see_stock(self):
        print('LIVRO:')
        print(f'Titulo:{self.titu}, Autor:{self.aut}, Preço: R${self.pre}, Quantidade em estoque:{self.quant}')

class Livraria:
    def __init__(self):
        self.bibli=[]

    def adicionar(self, item):
        self.bibli.append(item)
        
    def listar(self):
        return str(self.bibli)
    
    def desconto(self, cent, livro):
        if cent>0 and cent<100:
            new_pre=livro.pre*(cent/100)
            print(f'Preço do livro --{livro.titu}-- Após desconto: {new_pre}')
        else:
            print('Percentual de desconto inválido')
            
#testando a função de desconto da classe Livraria
livro1 = Livro('HP', 'JK', 10, 20)
livro2= Livro('HP', 'Jj', 10, 20)
livraria=Livraria()
livraria.adicionar(livro1)
livraria.adicionar(livro2)
print(livraria.listar())

livraria.desconto(10, livro1)
            
        