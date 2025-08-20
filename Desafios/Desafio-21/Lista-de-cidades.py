# Para este desafio, crie uma lista com os nomes de três cidades. Peça ao usuário para digitar on nome de uma cidade.
#Se a cidade estiver na lista, imprima "A cidade está na lista de cidades". Se a cidade não estiver na tupla, imprima
#"A cidade não está na lista de cidades".
#Obs. Você não pode utilizar list[]

tuple_cidades = ('Goiânia', 'Rio de Janeiro', 'Curitiba')
cidade_usuario = input('Digite uma cidade: ')

if cidade_usuario in tuple_cidades: 
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')