def somar(x):
    return x + 10

print(somar(2))

somar10 = lambda x,y: x + y + 10            # Funções lambda são funções "sem nome", geralmente são utilizadas DENTRO de funções já existentes.
print(somar10(2,4))                         # Funciona de forma parecida, só tive que adicionar a função lambda dentro de uma varíavel, já que ela não tem nome.