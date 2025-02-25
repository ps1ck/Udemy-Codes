aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 8.6, 'aprovação': True}

print(aluno['nome'])
aluno['nome'] = 'Jose'          # ATUALIZANDO um valor do dicionário por vez 
print(aluno['nome'])

aluno.update({'nome': 'João', 'idade': 15}) # ATUALIZANDO mais de um valor por vez, também pode atualizar um só se quiser.
print(aluno['nome'])
print(aluno['idade'])

aluno.update({'endereco': 'Rua A'})         # ADICIONANDO um item ao dicionario (sempre vai pra último)
print()
print(aluno)

print()
print(aluno.get('aniversario', 'Não informado'))    # Em vez de "print(aluno['aniversario'])", usamos isso para poder colocar
                                                    #uma mensagem de erro caso o endereço não exista.
aluno.update({'aniversario': '15/02/2010'})         # Aqui eu ADICIONEI a key(endereço) e o valor,
print(aluno.get('aniversario', 'Não informado'))    # ai aqui como existe, ele imprime sem problemas.

del aluno['nota_final']         # Basicamente deleta um item por vez.
print()
print(aluno)