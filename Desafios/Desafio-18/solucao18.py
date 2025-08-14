estoque = ['BMW X6', 'BMW i5', 'BMW i8']
pesquisa_carro = input('Digite o carro desejado: ')

if pesquisa_carro in estoque:                           # Bem mais simples e eficiente assim do que da forma que eu fiz
    print('O carro está disponível em estoque')
else:
    print('O carro não está disponível em estoque')
