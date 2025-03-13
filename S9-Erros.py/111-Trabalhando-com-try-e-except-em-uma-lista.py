try:                            # Ele vai tentar os códigos abaixo desta linha, se funcionar ele executa normal, se não vai pra linha do except.
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:              # Aqui você coloca o tipo de erro, nesse caso erro de index e coloca o que você quer que ele faça, pode ser uma mensagem etc. Eficiente
    print('Index errado!')      #pra ISOLAR os erros, pra que o programa continue executando e não pare nessa linha.