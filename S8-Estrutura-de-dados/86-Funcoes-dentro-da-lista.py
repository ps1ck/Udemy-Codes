# Na documentação do python tem as funções das listas
cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']              
                                                          
cidades.append('Santa Catarina')                                        # Adiciona um item ao FINAL da lista
cidades.remove('Salvador')                                              # Remove um item da lista, tem que digitar certinho aparentemente 
cidades.insert(1, 'Acre')                                               # Insere um item na posição especifica (pelo index), nesse caso foi 1, entrou no lugar de SP
cidades.pop(0)                                                          # Remove um item com base no INDEX, no caso foi o 0 então removeu RJ
cidades.sort()                                                          # Coloca a lista em ordem alfabetica (parece ter outros parametros pra isso, tem que olhar na 
                                                                        #documentação mais a fundo.
print(cidades) 

# Testando a ordem alfabetica de forma mais específica
letras = ['C', 'E', 'D', 'A', 'Z', 'G', 'H']
letras.sort()
print(letras)