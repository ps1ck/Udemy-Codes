rendimento = int(input("Qual é o rendimento da lata? "))    # Eu usei float porque apesar de estar digitando tudo em inteiro, o resultado
altura = int(input("Qual é a altura da parede? "))          #vai ser em float, então já preferi colocar assim no meu.
largura = int(input("Qual é a largura da parede? "))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()             # Da forma que ele escreveu a função ficou mais simples na hora de executar, e também mais fácil de ler. Mas como
                            #o resultado foi o mesmo e ele mesmo diz na aula que o importante é chegar no mesmo resultado usando o que foi 
                            #pedido, não vou considerar nenhum problema no meu código, só poderia ser um pouco melhor.