#Criei esse código pra testar o input
nome= input('Qual seu nome: ') #String
print ('Olá '+nome+'!')
manga = input('Qual seu mangá favorito: ') #String
capitulos = input('Em qual capítulo você está: ') #Inteiro
tempo = input('Quanto tempo demorou pra ler até ai (em horas): ') #Float, pode ser 2.5h por exemplo
desc = input('Dê uma breve descrição sobre o que você acha do mangá: ') #String

#Uma dúvida que eu tive agora que to escrevendo é como eu vou dizer pro input receber somente um inteiro, ou somente uma string, não sei...

print('O mangá favorito do '+nome+' é '+manga+', ele está no capítulo '+capitulos+' e demorou '+tempo+' horas pra chegar aqui.')
print('Agora uma breve descrição sobre o Mangá feita por ele: '+desc+'.')

#Funcionou impressionantemente bem! Porém na hora de printar eu deveria colocar o que é string e o que é inteiro pra que ele desse um erro caso a pessoa digitasse uma letra
#em vez de um número na variável tempo por exemplo, mas pra agora ta de bom tamanho.