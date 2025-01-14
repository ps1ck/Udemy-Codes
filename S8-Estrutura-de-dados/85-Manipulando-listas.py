cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']               # São separados pelo index, ou seja, rj é 0, sp é 1 e assim por diante.

print(cidades[0])                                                              # Printa Rio de Janeiro que tá no index 0
print(cidades[2])                                                              # Printa São paulo por que tá no index 2
print(cidades[-1])                                                             # Printa Goiania por que valores negativos de index começa da DIREITA pra ESQUERDA, ou seja
                                                                               #-1 é o 1° da direita pra esquerda, -2 é o 2° (Salvador) e assim por diante...
cidades[0] = 'Brasilia'                                                        # Mudei o item 0 (de acordo com o index) da lista cidades para 'Brasilia'
print(cidades[0])                                                              # Dai aqui em vez de imprimir Rio de Janeiro ele imprimiu Brasilia 
                                                                               #por que foi modificado anteriormente na linha 11.    
print(cidades)                                                                 # Aqui da pra ver a mudança de um item na lista toda.