import abc

class Conta(abc.ABC):

    

    @abc.abstractmethod
    def transferencia(self):
        pass

    @abc.abstractmethod
    def pagar(self):
        pass

    def getSenha(self):
        return self.__senha

    def setSenha(self,senha):
        self.__senha = senha
        return True