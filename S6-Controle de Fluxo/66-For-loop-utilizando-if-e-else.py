compra_confirmada = True
dados_compra = "Compra no valor de 12.50 e entrega confirmada"

for enviar in range(3):                                         # Um loop de 3x, ele vai verificar 3 vezes se a compra_confirmada = True, se for ele imprime o que foi pedido
    if compra_confirmada:                                       #e o comando BREAK faz ele sair do loop, se não tiver isso ele vai verificar e IMPRIMIR 3x, e a gente só quer
        print(dados_compra)                                     #uma verificação 3x, a partir do momento que for true ele tem que ter o break pra sair do loop
        print('Detalhes enviados para o seu email')             #E caso falhe as 3x vai pro else e imprime a falha, muito simples.
        break   
else: 
    print('Falha na compra')