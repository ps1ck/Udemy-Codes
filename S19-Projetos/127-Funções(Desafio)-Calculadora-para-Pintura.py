def calculoLatas(rendimento, altura, largura):
    resultado = (altura*largura) / rendimento
    print(f'Você precisa de {resultado} latas de tinta')

rLata = float(input("Qual é o rendimento da lata? "))
alturaParede = float(input("Qual é a altura da parede? "))
larguraParede = float(input("Qual é a largura da parede? "))
calculoLatas(rLata, alturaParede, larguraParede)