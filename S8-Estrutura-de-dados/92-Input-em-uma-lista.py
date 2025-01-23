frutas_usuario = input('Digite o nome das frutas separadas por vírgula: ')

frutas_lista = frutas_usuario.split(', ')                                       # Aqui ele usou o .split() pra separar as frutas digitadas em uma lista. Só que repare que
                                                                                #ele usou .split(', ') que significa que toda vez que o programa ver ', ' ele vai separar
print(frutas_lista)                                                             #o item, muito interessante..

print(frutas_usuario.split(', '))                                               # Quis testar dessa forma e funciona, mas no caso ele não armazena em nenhuma variável,
                                                                                #então seria só pra printar mesmo, depende do objetivo