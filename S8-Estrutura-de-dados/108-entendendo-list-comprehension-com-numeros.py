valores = []

for x in range(6):              # Jeito "normal" de se fazer o proposto (imprimir valores de 0 a 50 de 10 em 10).
    valores.append(x * 10)

print(valores)

valoresBetter = [x * 10 for x in range(6)]  # Exatamente o mesmo resultado, só que em uma linha única, bem eficiente.
            #   Expressão - for in range
print(valoresBetter)