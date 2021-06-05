import os, time, postgresql, abc
from datetime import date

class Login:

    cal = 0
    call = 0     
    ag = None

    def agencia(self):
                
        while self.cal <= 4 or self.cal >= 4:
            agen = str(input('AGÊNCIA : '))
            self.cal = len(agen)
            self.ag = agen
            if len(agen) == 4:
                break
            else:
                print('DADOS INCORRETO PERMITIDO APENAS 4 DIGITOS') 
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')   

        return agen

    def conta(self):        
        
        while self.call <= 6 or self.call >= 6:    
            cont = str(input('CONTA : ')) 
            self.call = len(cont)   
            if len(cont) == 6:
                break
            else:
                print('DADOS INCORRETO PERMITIDO APENAS 6 DIGITOS') 
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('AGÊNCIA : ',self.ag)    

        return cont


class Banco: 

    host = 'localhost'
    user = 'postgres'
    database = 'test'
    password = 'postgres'    
   

    def __init__(self):

        self.connect = postgresql.open(host = self.host, user = self.user, database = self.database, password = self.password) 
        
    def pesquisar_Login_contas(self,ag,numero): 

        query = f"SELECT * FROM contas WHERE agencia = '{ag}' and conta = '{numero}' "
        conne = self.connect
        usuario = conne.prepare(query)
        
        return usuario


class Validar_transferencia:
    X = 0
    Y = 0
    def transferencia_pergunta_banco(self):

        operacao = int(input('1- BANCO ITAU \n2- CAIXA ECONOMICA FEDERAL \n3- BANCO BRADESCO \n4- BANCO DO BRASIL\n'))
        if operacao == 1:
            X = 4
            Y = 6
            self.X = X
            self.Y = Y
        elif operacao == 2:
            X = 4
            Y = 9
            self.X = X
            self.Y = Y
        elif operacao == 3 or operacao == 4:
            X = 4
            Y = 11
            self.X = X
            self.Y = Y
        else:
            return False

    def validar_dados_banco(self):
        cal = 0
        print('INFORME OS DADOS PARA A TRANFERÊNCIA')
        while cal <= self.X or cal >= self.X:
            agen = str(input('AGÊNCIA : '))
            cal = len(agen)
            if len(agen) == self.X:
                break
            else:
                print(f'DADOS INCORRETO PERMITIDO APENAS {self.X} DIGITOS') 
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')  
                

        while cal <= self.Y or cal >= self.Y:    
            cont = str(input('CONTA : ')) 
            cal = len(cont)   
            if len(cont) == self.Y:
                break
            else:
                print(f'DADOS INCORRETO PERMITIDO APENAS {self.Y} DIGITOS') 
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')    
                print('AGÊNCIA :',agen)   


class Conta(abc.ABC):
    
    @abc.abstractmethod
    def transferencia(self):
        pass

class Corrente(Conta,Validar_transferencia):    

    senha = None
    def __init__(self):
        self.bank = Banco()

    def transferencia(self,saldo,senha,nume):
        data_atual = date.today()               
        desc = 'Transferência' 
        #descrição pro insert do historico

        num_conta = nume
        print(num_conta)
        self.senha = senha        
        print(f'saldo {saldo}')
        self.transferencia_pergunta_banco()
        self.validar_dados_banco()
        acao = int(input('1 - Continuar pra valor \n2 - Sair \n'))
        if acao == 1:
            print(f'saldo {saldo}')
            valor = float(input('Digite o valor da transferência : '))
            cont  = saldo - valor
            if cont >= 0:
                Senha = str(input('SENHA : ')) 
                if Senha == self.senha:     
                    ACAO = int(input('Confirmar Transferência\n 1 - Sim\n 2 - Não\n'))
                    if ACAO == 1:                                      
                        self.bank.update_Valor(cont,num_conta)                                        
                        print('TRANSFERÊNCIA EFETUADA COM SUCESSO')                        
                        #self.bank.ex(desc,num_conta,data_atual)
                        #usar o valor a conta  e puxa a data
                        self.bank.insert_historico(desc,valor,num_conta,data_atual)
                        #insert no historico
                        #update no banco com um valor novo
                    else:                        
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        print('Cancelando Transferência')
                        time.sleep(1.5)
                        pass
                else:
                    print('SENHA INCORRETA')
            elif cont < 0:
                print('SALDO INSUFICIENTE')                
        else:
            pass

    def pagar(self,saldo,senha,limCheqEsp,nume):  
        data_atual = date.today()   
        self.senha = senha   
        num_conta = nume
        desc = 'Pagamento'
        valor = str(input('Digite o valor do Pagamento : '))
        cont  = saldo - valor 
        print(cont)
        if (cont <= (saldo + limCheqEsp)):  
                          
            Senha = str(input('SENHA : ')) 
            if Senha == self.senha:     
                ACAO = int(input('Confirmar Pagamento\n 1 - Sim\n 2 - Não\n'))
                if ACAO == 1:  
                    print(cont)                                                  
                    self.bank.update_Valor(cont,num_conta)                                        
                    print('PAGAMENTO REALIZADO COM SUCESSO')        
                    self.bank.insert_historico(desc,valor,num_conta,data_atual)
            else:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Cancelando Pagamento')
                time.sleep(1.5)
                pass
        else:
            print("Valor informado maior que saldo atual.")

'''
#pede a agencia e conta
obj = Login()
Agencia = obj.agencia()
Conta = obj.conta()
'''

#puxa no banco se existe a agencia e a conta informada 
obj = Banco()
x = obj.pesquisar_Login_contas('0111','011111')
print(x()[0])

'''
if not x(): #valida se o retorno do banco esta ([] ou melhor dizendo null)
    print('Dados incorretos')
else:
    print('entrei...')

obj1 = corrente()
obj1.transferencia(1000,'12311','0111')

obj2 = obj1.Transferencia_valida_dados()
print(obj2[1])
'''
