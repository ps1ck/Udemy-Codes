# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em português. O usuário deverá
fornecer a temperatura.

Temperaturas - Cozimento 
120 °F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium Rare (Ao ponto para o mal)
140° ou 60°C - Medium (Ao ponto)
150° ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

# Antes de 48°C ele solicitou que o programa retorne -> Cozinhar por mais alguns minutos

ponto = int(input('Qual é a temperatura da carne?'))

if ponto < 48:
    print('Cozinhar por mais alguns minutos')
elif ponto >= 48 and ponto < 54:
    print('Selada')
elif ponto >= 54 and ponto < 60:
    print('Ao ponto para o mal')
elif ponto >= 60 and ponto < 65:
    print('Ao ponto')
elif ponto >= 65 and ponto < 71:
    print('Ao ponto para o bem')
else:
    print('Bem passada')