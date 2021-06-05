import postgresql



class Banco: 

    lista = {}

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
    
    def update_Valor(self,av,numero):
        query = f"UPDATE contas SET saldo = {av} WHERE conta = '{numero}' "
        conne = self.connect
        usuario = conne.execute(query)
        return usuario

    def insert_historico(self,descri,valo,con,dt):
        query = f"INSERT INTO historico (descricao_id,valor, conta_id, data_acao) VALUES ('{descri}',{valo},'{con}','{dt}') "
        conne = self.connect
        usuario = conne.execute(query)
        return usuario
    
    def extrato(self,a):
        query = f"SELECT * FROM historico WHERE conta_id = '{a}' "
        conne = self.connect
        usuario = conne.prepare(query)
        return usuario

    def historico(self,dado):
        
        lista_enca = {f"Informações da Transação: {dado[1]} | Data: '{dado[4]}' | Valor: {dado[2]}"}
        
        return lista_enca

