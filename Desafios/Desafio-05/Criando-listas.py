# Neste desafio, quero que você crie um script que solicite ao usuário dois números. Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação,
#a divisão (resultado decimal) e a exponenciação (primeiro número elevado ao segundo número) desses dois números.

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
divisao = num1 / num2 
exp = pow(num1, num2)

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {multi}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exp}')