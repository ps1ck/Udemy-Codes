palavra = "FANTASTICO"

for space in palavra:
    print(f' {space}' , end='')     # O comando end='' faz com que ele não pule uma linha e já vai pro próximo loop, assim a letra fica na horizontal, ele só vai parar 
                                    #quando não tiver mais nada ''. Ai usamos a formated strings e colocamos um espaço antes de cada palavra, ai chegamos no objetivo que
                                    #era transformar FANTASTICO EM  F A N T A S T I C O e qualquer outra palavra.