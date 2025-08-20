# Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países. Peça ao usuário para digitar
#o nome de um país. Se o país estiver na lista, imprima "A capital de [país] é [capital]". Se o país não estver na
#lista, imprima "Desculpe, não temos informações sobre a capital desse país".

paises = {
    'Brasil' : 'Brasília', 
    'Argentina' : 'Buenos Aires',
    'França' : 'Paris',
    'Rússia' : 'Moscou',
    'EUA' : 'Washington, D.C.'}

pais_usuario = input('Digite um país: ')

if pais_usuario in paises:
    print(f'A capital de {pais_usuario} é {paises[pais_usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país')