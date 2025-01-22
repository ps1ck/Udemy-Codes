numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)                  # Junta as duas listas, seria o mesmo de: "exemplo = numeros + letras" depois "print(exemplo)". Assim fica bem mais pratico
print(numeros)                      

LG = [['item1', 'item2'], ['item3', 'item4']]  # São duas listas dentro de uma lista geral (LG), da pra acessar cada lista e cada item pelo index

print(LG[0][0])                                # O primeiro [] é referente a lista, o segundo [] é referente a posição, então lista 0 (a 1°), item 0 ('item1')
print(LG[1][0])                                # [1] se refere a 2° lista, [0] se refere a 1° posição, no caso 'item3'
print(LG)                                      # Assim ele printa todas as listas de uma vez, repara que ele printa com os [], da pra ver que são 2 listas no console