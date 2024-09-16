mensagem = 'eu adoro comida Caseira'

print(mensagem.lower())         #tudo em minúscula
print(mensagem.upper())         #tudo em maiúscula
print(mensagem.capitalize())    #coloca a primeira letra em maiúscula
print(mensagem.find('c'))       #fala em qual posição no index está a letra c (minúscula), nesse caso 9
print(mensagem.find('C'))       #com a maiúscula agora ele da a posição 16
print(mensagem.find('adoro'))   #fala onde começa a palavra, nesse caso 3
print(mensagem.find('aDoro'))   #se eu errar a palavra ele printa -1, por que no caso não existe essa palavra
print(mensagem.replace('a', 'e'))#troca o caractere, na primeira aspas tem o antigo e no seugndo o que vai substituir
print(mensagem.replace('Caseira', 'feita em casa')) #também funciona com palavras

testeStrip = '               eu adoro petit gateau'

print(testeStrip)
print(mensagem.strip())     #remove os espaços

#toda vez que você digita por exemplo (mensagem.alguma coisa), da pra ir navegando entre os métodos, é bom dar uma checada
#depois o que cada um faz, vai que eu preciso de algum..