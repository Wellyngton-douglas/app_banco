from metodos import *
from validacao import *
from banco_app_banco import *
from datetime import date
from codigo_barra import *
import os, time

class Poupanca(Conta,Validar_transferencia,Codigo):    

    
    def __init__(self):
        self.bank = Banco() 
 
    def transferencia(self,saldo,nume):
        data_atual = date.today()               
        desc = 'Transferência' 
        #descrição pro insert do historico
        
        num_conta = nume            
        print(f'saldo {saldo}')
        self.transferencia_pergunta_banco()
        self.validar_dados_banco()
        acao = int(input('1 - Continuar pra valor \n2 - Sair \n'))
        if acao == 1:
            print(f'saldo {saldo}')
            valor = float(input('Digite o valor da transferência : '))
            cont  = (saldo - ( valor + 2.20))
            if cont >= 0:
                Senha = str(input('SENHA : ')) 
                if Senha == self.getSenha():     
                    ACAO = int(input('Confirmar Transferência\n 1 - Sim\n 2 - Não\n'))
                    if ACAO == 1:                                      
                        self.bank.update_Valor(cont,num_conta)                                        
                        print('TRANSFERÊNCIA EFETUADA COM SUCESSO')
                        self.bank.insert_historico(desc,valor,num_conta,data_atual)
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

    def pagar(self,saldo,nume):  
        data_atual = date.today()  
        num_conta = nume
        desc = 'Pagamento'
        valor = float(input('Digite o valor do Pagamento : '))
        cont  = (saldo - (valor + 3.10))
        if cont >= 0:   
            x = self.validar_cod()
            if x == True:              
                Senha = str(input('SENHA : ')) 
                if Senha == self.getSenha():     
                    ACAO = int(input('Confirmar Pagamento\n 1 - Sim\n 2 - Não\n'))
                    if ACAO == 1:                                   
                        self.bank.update_Valor(cont,num_conta)                                        
                        print('PAGAMENTO REALIZADO COM SUCESSO')        
                        self.bank.insert_historico(desc,valor,num_conta,data_atual)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print('Cancelando Pagamento')
                    time.sleep(1.5)
                    pass
            else:
                print('Código de Barra Incorreto')
        else:
            print("Valor informado maior que saldo atual.")