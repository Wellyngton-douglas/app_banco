import os, time

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

