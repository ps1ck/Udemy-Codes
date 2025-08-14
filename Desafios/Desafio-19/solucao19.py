while True:                                             # O while vai girar infinitamente, até cair naquele if e sair do loop, achei interessante a construção.
    fruta = input('Digite o nome de uma fruta: ')
    if fruta.lower() == 'abacate':
        break
        
print('Parabéns, você acertou a fruta!')