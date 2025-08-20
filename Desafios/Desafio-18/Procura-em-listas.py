# Para este desafio, imagine que você tem uma loja de carros. Crie uma lista com carros que você tem em estoque: BMW X6,
#BMW i5, BMW i8. Peça ao usuário para que ele insira o nome do carro que deseja comprar. Se o carro estiver em estoque,
#imprima "Este carro está disponível". Se o carro não estiver em estoque, imprima "Desculpe, este carro não está disponível".

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
        print('Desculpe, este carro não está disponível')       # Depois de ver a solução, lembrei que tem como colocar o IF pra percorrer
                                                                #os elementos da lista em vez de fazer um for...