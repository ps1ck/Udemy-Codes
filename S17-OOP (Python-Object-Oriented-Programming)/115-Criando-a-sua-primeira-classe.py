class Funcionarios:                             # Sempre começa com letra maiúscula e se quiser deixar a class vazia, escreva "pass".
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/2009'

usuario1 = Funcionarios()                       # Atribui a class a um objeto (usuario1)

print(usuario1.nome)                            # Puxei um dado da classe atraves do .
print(usuario1.sobrenome)
print(usuario1.data_nascimento)

# A utilização das classes geralmente é pra colocar funções, nesse caso aqui é somente pra ensinar mesmo, não é tão eficiente fazer isso porque se eu tiver muitos
#usuários eu ia ter que fazer isso pra cada um deles, o que demoraria DEMAIS.
# Então geralmente a class é usada mais ou menos assim:
# Class xxxxx:
    #def
        #xxxxxxxxxxxx
    #
    #def 
        #xxxxxxxxxxxxxx
    #def
        #xxxxxxx.......... 