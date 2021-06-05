import os, time

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
