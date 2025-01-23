cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:                        # Verifica se o que ele digitou esta dentro da lista de cores. Foi utilizada também a função .lower() pra definir 
    print('Em estoque')                                 #tudo que for digitado em letras minúsculas para que a verificação seja mais acertiva caso o usuário digite 'Azul'
else:                                                   #ou 'AMARELO' e etc.
    print('Não temos essa cor em estoque')