try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:                                        
    print('Favor digitar um valor em números')
else:                                                           
    print('O usuário digitou corretamente')                 # Else executa algo se a tentativa do try FUNCIONAR

print('========================================')

try:                          
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:             
    print('Index errado!')  
finally:
    print('Executa dando erro ou não')                      # Finally serve pra executar algo mesmo que o try funcione ou não, ele executa de qualquer jeito

print('Mais código abaixo')                                 