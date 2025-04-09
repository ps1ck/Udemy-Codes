import funcoes # Importa TODAS as funções que estão nesse módulo e tem que ser usado assim: funcoes.somar(). Se forem MUITAS funções e eu só for usar uma, vou acabar 
               #deixando o código mais lento desnecessáriamente.
funcoes.somar()
funcoes.multi()

# Pra deixar isso mais eficiente podemos usar:
from funcoes import somar, multi        # Consigo escolher quais funções quero importar, no caso de módulos com MUITAS funções deixa o código mais eficiente.
# E ai nesse caso, podemos usar a função chamando ela normalmente: (em vez de funcoes.somar()...)
somar()
multi()