# Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta. Se a fruta digitada não for 'abacate',
#o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta. Se a fruta for 'abacate', o loop deve terminar e 
#o programa deve imprimir "Parabéns, você acertou a fruta!".

resposta = input('Digite o nome de uma fruta: ')

while resposta.lower() != 'abacate':
    resposta = input('Fruta errada! Digite outra: ')        # O meu código da um retorno quando a pessoa erra, o dele não. Tirando isso, igual!

print('Parabéns, você acertou a fruta!')