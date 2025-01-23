cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

cores_list.append('roxo')       # A lista é mutable, pode ser modificada, adicionar itens, remover e etc. Por isso .append funciona sem erros.
print(cores_list)

cores_tuple.append('roxo')      # Já a Tuple é immutable, o que significa que ela não pode ser alterada, não pode adicionar, remover ou modificar nada nela, sempre fixa.
print(cores_tuple)              # Por isso deu erro, .append não pode ser usado em tuples pois ele adiciona um item

# O que ele resumiu no vídeo é: Se for uma lista que vai ser alterada, utilize listas, se for algo fixo, que vai ser mantido, use Tuples.  A tuple gasta menos 
#memória do que as listas, então é importante saber gerenciar qual tipo usar e etc.