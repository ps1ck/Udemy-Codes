dados = input('Digite o seu nome e idade: ').split() 
nome = dados [0] # Qualquer palavra digitada vai ser tratada como um "grupo" e vai para a posição 0, e a próxima pra posição 1 e assim por diante.
idade = dados [1]

print(f'Meu nome é {nome} e tenho {idade} anos de idade.')

#TESTE
print(f'Meu nome é {dados[0]} e tenho {dados[1]} anos de idade.') #Funciona também!!!