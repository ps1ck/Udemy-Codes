teste = 'teste'
print(list(teste))                                      # A função list() separa cada letra da STRING em UM item de uma lista..

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)                       # zip() junta as duas listas, mas ele da um valor que eu ainda não sei pra que serve, parece a posição da lista..
                                                        
print(duas_listas)
print(list(duas_listas))                                # Utilizamos o list() pra que ele imprima em forma de lista, ai temos as duas listas juntas, index 0 com 0, 1 com
                                                        #1 e assim por diante.
