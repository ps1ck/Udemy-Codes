idade = int(input("Digite sua idade: "))                                                 # No vídeo ele que coloca na mão a idade, mas acho que com input fica melhor

if idade >= 16:
    resultado = print('Voto Permitido (IfElse normal)')
else:
    resultado = print('Voto Não Permitido (IfElse normal)')


resultado = 'Voto permitido' if idade >= 16 else 'Voto Não Permitido'               # Bem mais eficiente, uma linha e tudo resolvido, muito útil pra if e else curtos.
print(f'{resultado} (Ternary Operator)')