class Codigo:
            
    def validar_cod(self):
        cod = str(input('Informe o Código de Barra\n'))
        if len(cod) == 47 or len(cod) == 48:
            return True
        else:
            return False





