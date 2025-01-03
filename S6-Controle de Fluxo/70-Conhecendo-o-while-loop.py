valor = 100
dia = 0 
while valor > 20:                                                           #Enquanto tiver uma condição o loop continua, é basicamente um loop com condição, sem mistério.
    dia+=1                                                                  #Aqui a gente soma +1 pra atualizar o dia.
    print(f'No dia {dia} o produto terá o valor de: {valor} reais')         
    valor-=5                                                                #E aqui a gente reduz 5 pra aplicar o desconto todo dia E também porque o valor tem que chegar
                                                                            # em 20 se não fica um loop infinito.