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