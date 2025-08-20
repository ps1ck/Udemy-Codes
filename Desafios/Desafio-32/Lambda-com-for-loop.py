# Para este desafio, crie uma função lambda que eleve um número ao quadrado. Em seguida, use essa função para
#calcular o quadrado de todos os números em uma lista usando um loop for.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = lambda x: x**2
resultados = []

for i in numeros:
    resultados.append(quadrado(i))

for i in range(0,len(resultados)):  # Basicamente pra ficar uma saída mais bonitinha mesmo :)
    print(f'O quadrado de {numeros[i]} é {resultados[i]}')