def soma(*numeros):         #O * antes significa que o número de argumentos a serem passados é variável, pode ser 1,2,5,10, tanto faz. XARGS o nome disso parece.        
    resultado = 0           #Resultado se inicia em 0 pra poder somar com os números que vierem, se não fizer isso é como se ele fosse somar "nada" com o que vier, erro.
    for num in numeros:     #Vai pegar cada numero que for passado no argumento (linha 8) e somar com o resultado(que começa com 0) e ai ele retorna o resultado e soma
        resultado += num    # de novo, até acabar todos os números.
    return resultado


x = soma(2,3,4,7)           #Chamo a função
print(x)                    #Imprimo o VALOR da função