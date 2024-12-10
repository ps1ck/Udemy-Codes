valor = 25

if valor >= 20 and valor < 40:
    print('Produto foi aceito')
else:
    print('Produto não aceito')

# Uma maneira mais resumida e matemática de fazer essa verificação é trocando "valor >= 20 and valor < 40" por somente "20 <= valor < 40"

if 20 <= valor < 40:                   # Desse jeito não precisa do and entre as expressões e nem repetir, fica mais facil, mas provavelmente
    print('Produto foi aceito')        #só vale pra valores matemáticos, números, por ser maior que, menor que e etc.. (A não ser que seja
else:                                  #tipo tamanho de string e tal, mas isso seria mais pra frente..)
    print('Produto não aceito')                                   
                                    
# Basicamente colocar o valor entre os dois operadores, mais simples pra visualizar o range que eu quero que o valor esteja