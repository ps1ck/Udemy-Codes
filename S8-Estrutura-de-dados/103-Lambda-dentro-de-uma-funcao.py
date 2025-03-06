def somar(x):
    func2 = lambda x: x + 10            # Criei uma função "sem nome" dentro de uma função. Na aula ele explicou que é dificil ver um porque eu faria isso no momento, mas é
    return func2(x) * 4                 #porque essa é uma função simples que poderia ser resolvida em uma linha, mas em funções mais complexas, criar uma "subfunção" pode
                                        #ser muito útil. Na linha 3 eu chamei a função lambda e coloquei o x como argumento, que no caso é 2, ai ele fez 2 + 10 (função lambda)
print(somar(2))                         #e depois * 4,resultando em 48.    