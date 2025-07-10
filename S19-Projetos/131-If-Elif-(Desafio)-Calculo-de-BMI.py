# Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm: 
Qual é o seu peso em kg: 
'''

# MENOR QUE 18,5        MAGREZA
# ENTRE 18,5 E 24,9     NORMAL
# ENTRE 25,0 E 29,9     SOBREPESO
# ENTRE 30,0 E 39,9     OBESIDADE
# MAIOR QUE 40,00       OBESIDADE GRAVE

def IMC(peso, altura):
    imc = peso / pow(altura/100,2)
    imc = round(imc, 1)             # Para evitar a falha de calculo. Explicado melhor no código de solução!
    if imc < 18.5:
        print(f'IMC = {imc:.1f}\nVocê está magro!') # Saída do meu código ficou mais completa que a da solução, mas a ideia era só ensinar mesmo.
    elif imc >= 18.5 and imc <= 24.9:
        print(f'IMC = {imc:.1f}\nVocê está no peso NORMAL!')
    elif imc >= 25.0 and imc <= 29.9:
        print(f'IMC = {imc:.1f}\nVocê está com sobrepeso!')
    elif imc >= 30.0 and imc <= 39.9:
        print(f'IMC = {imc:.1f}\nVocê está obeso!')
    elif imc >= 40.0:
        print(f'IMC = {imc:.1f}\nVocê está com obesidade GRAVE!')
    else:
        print('Classificação não identificada.') 
alturaUsuario = float(input('Qual é a sua altura em cm: '))
pesoUsuario = float(input('Qual é seu peso em kg: '))
IMC(pesoUsuario, alturaUsuario)