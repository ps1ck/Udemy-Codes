produtos= ['arroz', 'feijao', 'laranja', 'banana']
produtosNew = ['arroz', 'feijao', 'laranja', 'banana', 5,6,7,8]

item1, item2, item3, item4 = produtos           # Você pode usar variáveis pra armazenar cada item da lista, só que se a lista tem 4 itens, desse jeito aqui você tem que
print(item1, item2, item3, item4)               #colocar 4 variáveis pra funcionar..

item1, item2, item3, *outros = produtosNew      # Aqui essa lista tem 8 itens mas eu só quero armazenar em 3 itens, então eu coloquei até o item3 e o resto eu coloquei
print(item1, item2, item3, outros)              #*outros, o * significa que pode ter um número indeterminado de itens e todos eles estão em outros, da pra verificar
                                                #melhor isso olhando o console, ele printa as variáveis que eu pedi e todo o resto da variável outros

item1, item2, *outros, item8 = produtosNew      # Aqui é o mesmo conceito só que peguei 2 itens no começo e 1 item no final, e o meio ficou como "resto"
print(item1, item2, outros, item8)              # Único problema que encontrei nisso é que: E se eu quiser pegar 4 números bem no meio da lista? Vou tentar solucionar..


meioDaLista = [1,2,3,4,5,6,7,8,9,10]
cinco = meioDaLista[4]                          # Pelas minhas tentativas o único jeito seria esse, na mão mesmo, um por um...
seis = meioDaLista[5]
sete = meioDaLista[6]
print(cinco,seis,sete)
