# Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos. Alguns nomes devem estar presentes
#em ambos os conjuntos. Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.

set_amigos = {'Gustavo', 'Rafael', 'Lavínia', 'Pedro', 'Arthur'}
set_amigos2 = {'Ricardo', 'Rafael', 'Gustavo', 'Pedro', 'Augusto'}

print(set_amigos & set_amigos2)     # & = intersection / and. Imprime o que se repete nos dois sets