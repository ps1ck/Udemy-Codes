valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(map(remover20, valores)))    # Aqui ele imprime com False e True.

print(list(filter(remover20, valores))) # Utilizando o filter ele imprime somente os números que são True. Nesse caso filtrando números acima de 20, de acordo com a função.

print(list(filter(lambda x: x > 20, valores)))  # A mesma coisa só que com Lambda, beeem mais simples e fácil.