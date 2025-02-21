#DESCONTOS

valor = int(input('Digite o valor da compra: '))
desconto = 0.05      #Valor mínimo, em qualquer compra

if valor > 100 and valor <= 200:
    desconto = 0.10 #10%
elif valor > 200:
    desconto = 0.20 #20%

valorFinal = valor - (valor*desconto)
print(f'O valor final é de R$ {valorFinal:.2f}')