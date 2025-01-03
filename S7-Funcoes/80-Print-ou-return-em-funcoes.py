# Diferença entre print e return

def cliente1(nome):
    print(f'Olá {nome}')    # Aqui a função é apenas imprimir, nada é armazenado na memória.


def cliente2(nome):
    return f'Olá {nome}'    # Aqui o return não IMPRIME o valor ele apenas o armazena na função.


cliente2('Marcos')          # Por isso aqui ele não faz NADA quando eu chamo a função, porque ela só tem um valor ARMAZENADO e não é pra ser IMPRESSO
print(cliente2('Marcos'))   # Aqui eu solicitei que fosse IMPRESSO (print) o valor ARMAZENADO (pelo Return), então assim foi feito.

print(' ')                  # Só pra separar e melhorar a visualização no console

cliente1('João')            # Aqui ele já imprime porque a função É imprimir.
print(cliente1('João'))     # Aqui eu to solicitando o valor da função que teria que estar ARMAZENADO (usando o Return), como não tem nada ARMAZENADO ele faz a função
                            #que no caso é imprimir o Olá com o nome e logo depois diz "none", porque não tem nenhum VALOR ARMAZENADO na função, porque é usado o print
                            #e não o Return dentro da função.