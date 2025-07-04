#Desafio usando 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

func = set(funcionarios)
dia = set(turno_dia)
noite = set(turno_noite)
carro = set(tem_carro)

print('Funcionários que tem carro e trabalham a noite: ')
print(carro & noite)
print('Funcionários que tem carro e trabalham de dia: ')
print(carro & dia)
print('Funcionários que não tem carro: ')
print(func ^ carro)

