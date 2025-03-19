class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):       # Criando uma função construtora, self é o objeto que vai mudar, no caso usuario1,2,3.. e nome, sobrenome,
        self.nome = nome                                        #data.. são os argumentos, igual criar uma função normal, passa os argumentos pra usar os parametros depois.
        self.sobrenome = sobrenome                              
        self.data_nascimento = data_nascimento

usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')        # Aqui ficou bem mais simplificado, eu criei o objeto e já passei os parametros, ou seja, criamos um objeto,
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')         #já colocamos os dados necessários, cada um em somente UMA linha. Isso ta ficando interessante...
usuario3 = Funcionarios('Andre', 'Iacono', '11/03/2003')

print(usuario1.nome)
print(usuario2.nome)
print(usuario3.data_nascimento)