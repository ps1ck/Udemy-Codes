#Quero tentar fazer um triangulo no console

altura = 10  # Altura do triângulo
sb = '#'    # Símbolo do triângulo
sb2 = ' '   # Espaço vazio

for x in range(1, altura + 1):
    espacos = sb2 * (altura - x)  # Espaços antes do símbolo
    simbolos = sb * (2 * x - 1)   # Símbolos na linha
    print(f'{espacos}{simbolos}{espacos}')



# Usei o chat GPT pra melhorar meu codigo e me ensinar direito, entendi que o x começa com 1 e soma 1 a cada iteração, só fazer a conta na cabeça ai agora que da pra
#ver que funciona perfeitamente, genial.
