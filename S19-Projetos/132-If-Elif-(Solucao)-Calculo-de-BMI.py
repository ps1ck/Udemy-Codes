altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2        # Como ele não fez função, economizou mais linhas.

if IMC < 18.5:
    print('Magreza')
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')

# Porém esse código, quando digita por exemplo, 178 e 95kg, da obesidade grave, quando na verdade é somente obesidade, isso acontece porque
# o python tem um problema aparentemente comum quando se trata de calculos com ponto flutuante, pra resolver isso o gpt me disse pra usar o
# round que usei no meu código, arredondando os valores depois do ponto e fazendo a conta ficar mais precisa. Fazer também um elif para o 
# obesidade grave e só pra caso de erros colocar o else. Assim funcionou perfeitamente! No geral esse ficou um código mais simples e 
# menos detalhado nas saídas, mas tirando o erro deu na mesma.