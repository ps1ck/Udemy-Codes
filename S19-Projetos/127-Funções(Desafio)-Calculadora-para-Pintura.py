# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

def calculoLatas(rendimento, altura, largura):
    resultado = (altura*largura) / rendimento
    print(f'Você precisa de {resultado} latas de tinta')

rLata = float(input("Qual é o rendimento da lata? "))
alturaParede = float(input("Qual é a altura da parede? "))
larguraParede = float(input("Qual é a largura da parede? "))
calculoLatas(rLata, alturaParede, larguraParede)