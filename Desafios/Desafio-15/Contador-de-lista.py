# Para este desafio, crie uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua escolha. use um loop for para contar
# quantas vezes "maçã" aparece na lista e imprima o resultado.

frutas = ['Maçã', 'Maçã', 'Maçã', 'Banana', 'Morango', 'Uva']
contador = 0

for fruta in frutas:
    if fruta == 'Maçã':
        contador += 1

print(f'A fruta Maçã aparece {contador} vezes na lista')