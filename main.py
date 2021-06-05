from corrente import *
from poupanca import *
from login import * 


i = 0

sistema = True

#pede a agencia e conta
obj_login = Login()
Agencia = obj_login.agencia()
Conta = obj_login.conta()
Senha = str(input('SENHA : '))   

while sistema == True:

    try:            
        
        #puxa no banco se existe a agencia e a conta informada 
        obj_banco = Banco()
        obj1 = obj_banco.pesquisar_Login_contas(Agencia,Conta)

        #puxa as acoes de corrente e poupança
        obj_corrente = Corrente()
        obj_poupanca = Poupanca()
        

        #puxa o historico 
        ex = obj_banco.extrato(Conta)

        if not obj1(): #valida se o retorno do banco esta ([] ou melhor dizendo null)
            print('Dados incorretos')
        elif (Conta == obj1()[0][4]) and (Senha == obj1()[0][2]) and (obj1()[0][7] == 'Corrente'):
            os.system('cls' if os.name == 'nt' else 'clear')
            obj_corrente.setSenha(Senha)
            acao = int(input('1-extrato\n2-transações\n3-serviços\n4-desconectar\n'))
            if acao == 1: 
                os.system('cls' if os.name == 'nt' else 'clear') 
                contador = 1
                for dado in ex:
                    print(contador,obj_banco.historico(dado))
                    contador += 1                
                acao = int(input('1- Voltar \n2- Sair\n'))
                if acao == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.5)
                    pass
                else:
                    exit()
            elif acao == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                mov = int(input('1 - Pagamento\n2 - Transferência\n3 - Voltar\n'))
                if mov == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    obj_corrente.pagar(obj1()[0][6],obj1()[0][5],obj1()[0][4])
                    time.sleep(1.5)
                elif mov == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    obj_corrente.transferencia(obj1()[0][6],obj1()[0][4])
                    time.sleep(1.5)
                else:
                    time.sleep(1.5)
                    pass
            elif acao == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                mov = int(input('1 - Limite Emergencial\n2 - Cartões\n3 - Voltar\n'))
                if mov == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Seu limite emergencial é:',obj1()[0][5])
                    time.sleep(1.5)
                    pass
                elif mov == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Seu Cartão Ainda Não Foi Aprovado')
                    time.sleep(1.5)
                    pass
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.5)
                    pass
            else:
                sistema = False


        elif (Conta == obj1()[0][4]) and (Senha == obj1()[0][2]) and (obj1()[0][7] == 'Poupança'):
            os.system('cls' if os.name == 'nt' else 'clear')
            obj_poupanca.setSenha(Senha)
            acao = int(input('1-extrato\n2-transações\n3-desconectar\n'))
            if acao == 1: 
                os.system('cls' if os.name == 'nt' else 'clear')
                contador = 1
                for dado in ex:
                    print(contador,obj_banco.historico(dado))
                    contador += 1
                acao = int(input('1- Voltar \n2- Sair\n'))
                if acao == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.5)
                    pass
                else:
                    exit()
            elif acao == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                mov = int(input('1 - Pagamento\n2 - Transferência\n3 - Voltar\n'))
                if mov == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    obj_poupanca.pagar(obj1()[0][6],obj1()[0][4])
                    time.sleep(1.5)
                elif mov == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    obj_poupanca.transferencia(obj1()[0][6],obj1()[0][4])
                    time.sleep(1.5)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.5)
                    pass
            else:
                sistema = False


    except(ValueError, TypeError):
            print('Tivemos um problema com o tipo de dado informado')