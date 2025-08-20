# Para este desafio, crie uma lista de números de 1 a 10. use um 'for loop' para iterar sobre a lista. Se o número atual da 
#iteração for par, imprima "O número [número] é par. Se o número for ímpar, imprima "O número [número] é ímpar".

for number in range(1,11):
    if (number%2) == 0:
        print(f'O número {number} é par')
    else:
        print(f'O número {number} é ímpar')