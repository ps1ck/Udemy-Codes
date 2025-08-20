# Para este desafio, crie uma função que calcule a potência de um número. A função deve aceitar dois argumentos: a base
#e o expoente. No entanto, se o expoente não for fornecido ao chamar a função, ele deve assumir o valor padrão de 2.

def potencia(base, exp=2):
    return base ** exp

user_base = int(input("Digite a base da potência: "))
user_exp = input("Digite o expoente da potência (default=2): ") # Deixando só como input e passando pra int na hora da conta,
                                                                #conseguimos não receber valor aqui.

if user_exp:
    print(f'O resultado da potência({user_base} ** {user_exp}) é: {potencia(user_base,int(user_exp))}')
else:
    print(f'O resultado da potência({user_base} ** 2) é: {potencia(user_base)}')