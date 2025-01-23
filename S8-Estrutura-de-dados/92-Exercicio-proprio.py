numeros = input('Digite os numeros separados por vírgula por favor: ')

listaN = numeros.split(', ')

for num in listaN:
    x = int(num)                        # Tem que fazer isso se não da erro por tentar comparar uma string com um int (x > 10). Aqui eu transformo toda vez em int, antes.
    if x > 10:
        print(f'{x} é maior que 10')
    else:
        print(f'{x} é menor que 10')