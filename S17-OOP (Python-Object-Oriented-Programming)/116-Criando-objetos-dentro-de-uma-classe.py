# Criando a classe
class Funcionarios:
    pass                                    # Basicamente uma classe vazia, o pass faz com que só "passe" o código e leia o que tem em baixo.

# Criando os objetos
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# Criando os parametros do usuario1
usuario1.nome = 'Elena'                     # Dessa maneira eu consigo separar por usuário, anteriormente todas as informações estavam dentro da classe, agora estão cada um
usuario1.sobrenome = 'Cabral'               #em um usuario diferente.
usuario1.data_nascimento = '12/01/2009'

# Criando os parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '15/10/2005'

# Print
print(usuario1.nome)
print(usuario2.data_nascimento)