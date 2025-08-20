# Para este desafio, crie uma função lambda que aceite os dois números e retorne a multiplicação desses números.

multi = lambda num, num2: num * num2
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
print(f'Resultado da multiplicação: {num1} x {num2} = {multi(num1,num2)}')