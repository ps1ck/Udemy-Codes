carros = ['BMW X6', 'BMW i5', 'BMW i8']

pedido = input('Qual carro você deseja? ')
indisponiv = 0

for carro in carros:
    if pedido == carro:
        print('Este carro está disponível')
        break
    else:
        indisponiv += 1

    if indisponiv == 3:
        print('Desculpe, este carro não está disponível')       # Depois de ver a solução, lembrei que tem como colocar o IF pra percorrer os elementos da lista em vez de fazer um for...