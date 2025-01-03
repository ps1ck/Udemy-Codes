def soma():
    numero1 = 10                        # Todas as variáveis declaradas dentro de uma função são exlcusivas delas, não posso acessar elas fora da função
    numero2 = 5                         # O que significa que também posso repetir o nome delas em OUTRAS funções ou em outras áreas do meu código sem
    resultado = numero1 + numero2       #nenhuma relação.
    print(resultado)
                                        # No curso ele disse que sempre após uma função é bom pular DUAS linhas pra escrever algo.

def soma1():
    numero1 = 10                  
    numero2 = 2                       
    resultado = numero1 + numero2       
    print(resultado)

soma()
soma1()
#print(resultado)                        # Da erro porque essa variável só existe dentro da função soma().