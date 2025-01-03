# Código usado na aula:

x = str (3)
y = int (4)
z = float(5)

print (x + x) #Ele imprime 33 por que não trata o 3 como número, trata como texto, ai sai os dois juntos
print (y + y) #Imprime 8 por que foi tratado como número inteiro e 4 + 4 = 8 
print (z + z) #Imprime 10.0 por que foi tratado como fração, número decimal, a conta fica 5.0 + 5.0 = 10.0

#Quero testar se posso modificar o tipo da variavel somente na hora de imprimir, muitas vezes é preciso usar a mesma variável pra fazer coisas diferentes
a = 75
print (a + a) #Saiu 150 (resultado de 75 + 75)
print (str(a) + str(a)) #Saiu 7575, assim como eu esperava, acertei a sintaxe de primeira :)
