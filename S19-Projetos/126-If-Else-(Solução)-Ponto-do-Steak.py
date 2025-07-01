# Solução do professor!

tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')
elif tem_cel in range(48, 53):                          # Usar in range é mais precis e mais fácil de visualizar.
    print('Selada')
elif tem_cel in range(54, 59):
    print('Ao ponto para o mal')
elif tem_cel in range(60, 64):
    print('Ao ponto')
elif tem_cel in range(65, 70):
    print('Ao ponto para o bem')
elif tem_cel >= 71:                                     # Nesse ele até tinha colocado o Else e mudou depois, eu coloquei pois achei que era
    print('Bem passada')                                #obrigatório usar.... Mas o resultado foi o mesmo, então tudo certo.