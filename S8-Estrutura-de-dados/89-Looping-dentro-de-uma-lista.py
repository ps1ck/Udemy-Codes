valores = [50, 80, 110, 150, 170]

for x in valores: 
    print(f' O valor final do produto é de R${x}')              # Vai puxar todos os itens da lista até acabar e colocar nessa frase, interessante.


for teste in valores:                                           # Quis fazer um teste por conta própria de if no for com listas e deu certo! :)
    if teste > 100:
        print(f'O valor final do produto é de R${teste}')
    else:
        print('Valor baixo demais')