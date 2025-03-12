frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

for item in frutas1:            # Pega os itens que tem 'b' e adiciona na lista frutas2.
    if 'b' in item:
        frutas2.append(item)        

print(frutas2)

frutas2better = [item for item in frutas1 if 'b' in item] # Mesma coisa do de cima só que mais eficiente e em uma única linha.
print(frutas2better)

# Segundo a aula, funciona assim: [expresão for iten in itens]
# Pelo que eu entendi, a expresão é o que ta dentro do .append, é o que ele deve fazer. (Explica melhor na próx aula)