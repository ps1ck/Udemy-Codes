def agencia(**carro):                           #Os 2 * significam que eu posso passar tanto os ARGUMENTOS quanto os PARÂMETROS lá em baixo, tudo pode ser variável, é a
    return carro                                # mesma função só que eu posso usar parâmetros e argumentos diferentes toda vez que eu CHAMAR ela, bem versátil.


print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='Gol', cor='Azul', motor=1.0))
print(agencia(marca='Gol', cor='Preto'))