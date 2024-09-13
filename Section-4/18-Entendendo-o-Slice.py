fruta = 'Abacate'
#index   0123456 
# pode ser assim ou assim:
#index   7-6-5-4-3-2-1 (invertido, serve pra pegar uma parte de algo muito grande que ta no final, só colocar -1)
print(fruta[0]) #Imprime só o A
print(fruta[3]) #Imprime só o C
print(fruta[2:5]) #Imprime de 2 até o 5, porem o python imprime sempre a primeira letra mas a útilma ele não imprime (nesse caso o 5), então se eu quiser mostrar a letra 5
                  # eu vou ter que colocar uma a frente, segue como a baixo:
print(fruta[2:6])
# e se eu quiser mostrar a ultima letra tenho que colocar 7 que teoricamente estaria fora do index mas é a última letra
print(fruta[2:7])
# exemplo do index negativo
print(fruta[-1]) #Imprime só a letra "e", que é a primeira na contagem inversa


# com números agora:
valor = 99.75
#por ser um número eu tenho que transforma-lo em string pra poder pegar uma parte, posso fazer assim:
print(str(valor)[0:2]) #aqui eu mudei só na hora de imprimir, "valor" continua sendo um float
#        OU
valor = str(valor) #aqui eu mudei pra float antes de imprimir, só que eu mudei a variável "valor" de FLOAT pra STRING, então daqui pra baixo toda vez que eu der um print
print(valor[0:2])  #com essa variável eu preciso lembrar que ela é uma string.
