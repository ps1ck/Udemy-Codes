#Default = Aquele que você define o valor no parâmetro
#Non-Default = Aquele que você não define o valor no parâmetro

def boasvindas(nome, quantidade=6):                     # Defini um valor DEFAULT para a variável quantidade, SE eu NÃO passar nenhum argumento a função vai usar
    print(f'Olá {nome}!')                               #o 6, mas SE eu PASSAR um argumento ela vai subescrever o 6, é só pra não causar erro caso nada seja passado como
    print(f'Temos {quantidade} laptops em estoque')     #argumento, definir um valor padrão.


boasvindas('Marcos')                                    

'''
SUPER IMPORTANTE: Toda vez que for definir os valores Non-Default e Default na função a gente deve OBRIGATÓRIAMENTE passar as Non-Default PRIMEIRO, ou seja as que não tem
valor pré-definido, caso isso não seja feito o programa vai dar erro. Se você tentar definir um valor, colocar um default antes de um non-default no parâmetro ele vai dar 
ERRO, sempre sempre LEMBRE-SE -> Non-Default PRIMEIRO e depois DEFAULT.

EXEMPLO CORRETO -> def boasvindas(nome, quantidade=5)
EXEMPLO ERRADO  -> def boasvindas(nome='Marcos', quantidade) -> repare que eu defini 'Marcos' como argumento Default pra nome, só que logo depois vem a variável quantidade
que é um valor NON-DEFAULT, ou seja, precisa ser declarado, isso vai dar erro porque os argumentos pré-setados, DEFAULTS devem vir DEPOIS dos NONDEFAULTS, igual no primeiro
exemplo.
'''