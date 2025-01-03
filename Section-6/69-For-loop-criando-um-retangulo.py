linhas = 6
colunas = 6
simbolos = "@"

for l in range(linhas):                 # Toda vez que esse Outer Loop acontece ele imprime o Inner Loop 6x na mesma linha por causa do "end=''" e ele pula uma linha
    for c in range(colunas):            #antes de começar o OuterLoop de novo por causa do "print()" que ta vazio ali no final, então o processo é imprimir 6 @ do inner
        print(simbolos, end='')         #loop imprimir uma casa vazia e voltar pro outerloop depois inner loop, casa vazia, e assim vai...
    print()