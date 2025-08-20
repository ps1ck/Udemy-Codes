# Para este desafio, crie uma lista de frutas e outra de vegetais. Use um "for loop" aninhado (Nested for loop) para imprimir todas as combinações 
#posssíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.

frutas = ['Maçã', 'Banana', 'Manga']
vegetais = ['Cenoura', 'Alface', 'Brocolis']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)