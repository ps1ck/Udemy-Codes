from datetime import datetime                               # Importamos isso pra pegar o ano atual de forma automática

class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):    # Trocamos de data para ano, para facilitar o calculo
        self.nome = nome                                        
        self.sobrenome = sobrenome                              
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):                                
        return self.nome + ' ' + self.sobrenome          

    def idade_funcionario(self):                                        
           ano_atual = datetime.now().year                                 # Primeiro definimos o ano atual com esse "datetime" que foi importado no início.
           self.ano_nascimento = int(ano_atual - self.ano_nascimento)      # Depois colocamos o ano atual - o ano de nascimento do funcionário. Importante colocar como int()!!
           return self.ano_nascimento                                      # E retornamos o resultado.
                                                            
usuario1 = Funcionarios('Elena', 'Cabral', 2009)        
usuario2 = Funcionarios('Carol', 'Silva', 2005)         
usuario3 = Funcionarios('Andre', 'Iacono', 2003)
                         
print(Funcionarios.idade_funcionario(usuario1))     
print(Funcionarios.idade_funcionario(usuario2)) 
print(Funcionarios.idade_funcionario(usuario3))             