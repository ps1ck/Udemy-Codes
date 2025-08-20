# Para este desafio, quero que você crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando
#o comando "break". Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão do número 5 usando o 
#comando "continue".

for number in range(1,11):
    if number > 5:
        break
    print(number)

print()

for number in range(1,11):
    if number == 5:
        continue
    print(number)