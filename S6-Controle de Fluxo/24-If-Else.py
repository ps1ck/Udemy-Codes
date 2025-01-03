velocidade = input('Velocidade do veículo: ') #Na aula ele não coloca um input, muda na mão, mas eu quis fazer assim, da na mesma

if int(velocidade) > 110:                               # Aqui eu coloquei int pra poder fazer a comparação, >, < essas coisa
    print('Acima da velocidade permitida.')             #não podem ser usadas com strings.
    print('Favor reduzir a sua velocidade.')
elif int(velocidade) < 60:
    print('Favor dirigir acima de 80Km/h.')
else:
    print('Velocidade OK.')
# Diferente de outras linguagens o if else ficou mais simples, tudo que da identado (4 espaços pra frente fazem parte do if,
#elif, else). Isso ajuda bastante em vez de ficar com aquele tanto de paragrafo que geralmente fica nas outras linguagens.
# Além de poder colocar quantos "Elif" eu quiser, em vez de criar if dentro de if é só colocar o elif, tem que tomar cuidado
#com as condições pra não dar erros, mas ajuda bastante, vou tentar colocar um if dentro de outro pra ver como funciona, na
#aula ele não disse nada sobre

testeif = input('Digite um número: ')

if float(testeif) > 20:
    if float(testeif) == 25:
        print('O número é 25!')
    else:
        print('Número é maior que 20, mas não é 25.')
else:
    print('O número não é maior que 20.')

# Funcionou mt bem, só tem que prestar atenção na identação que tudo flue bem, python parece mesmo bem simples como dizem.
