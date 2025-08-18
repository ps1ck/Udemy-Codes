tuple_cidades = ('Goiânia', 'Rio de Janeiro', 'Curitiba')
cidade_usuario = input('Digite uma cidade: ')

if cidade_usuario in tuple_cidades: 
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')