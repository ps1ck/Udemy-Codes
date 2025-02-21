#SAUDAÇÕES

horario = int(input('Digite a hora do dia no formato 24h: '))

if horario >= 6 and horario < 12:
    print('Bom dia')
elif horario >=12 and horario < 18:
    print('Boa tarde')
else:
    print('Boa noite')