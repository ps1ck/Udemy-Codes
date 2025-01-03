for numero1 in range(1,6):                  # Esse loop roda uma vez e o de dentro roda 10x, ai esse roda denovo 1x, o de dentro roda 10x, e assim se repete até o de fora
    print('Produto '+ str(numero1))         #acabar, da pra criar varias listas usando esse código aqui, muito interessante
    for numero2 in range(11):
        print(numero1, numero2)             # Outer Loop = é o loop de fora     
                                            # Inner Loop = é o loop de dentro
                                            # Nesse exemplo, toda vez que o Outer Loop girar 1x o Inner Loop vai rodar 10x até o Outer Loop concluir 5x (seu range)