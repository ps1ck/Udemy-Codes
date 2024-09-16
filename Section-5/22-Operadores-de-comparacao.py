#Operador EQUAL ==
equal = 'banana' == 'banana' #True
equalf = 'banana' == 'Banana' #False
equal2 = 10 == 10 #True
equalf2 = 10 == 11 #False
print('- EQUAL:')
print(equal,equalf,equal2,equalf2)

#Operador NOT EQUAL !=
notEqual = 'morango' != 'Morango'  #True por que eles não são iguais (not equal)
notEqualf = 'morango' != 'morango' #Dá false por que os dois são iguais
print('- NOT EQUAL:')
print(notEqual,notEqualf)

#Operador Greater than / Maior que
greaterf = 10 > 11   #False
greater = 10 > 2     #True
print('- GREATER THAN:')
print(greaterf,greater)

#Operador Less than / Menor que
lessf = 11 < 2  #False
less = 7 < 20 #True
print('- LESS THAN:')
print(lessf,less)

#Operador greater than or equal to / Maior ou igual
greaterequal = 10 >= 1 #True
greaterequal2 = 10 >= 10 #True
greaterequalf = 10 >= 30 #False
print('- GREATER THAN OR EQUAL TO:')
print(greaterequal,greaterequal2,greaterequalf)

#Operador less than or equal to / Menor ou igual
lessequal = 10 <= 20 #True
lessequal2 = 10 <= 10 #True
lessequalf = 10 <= 1 #False
print('- LESS THAN OR EQUAL TO:')
print(lessequal,lessequal2,lessequalf)