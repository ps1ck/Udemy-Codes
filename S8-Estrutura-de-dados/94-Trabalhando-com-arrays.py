from array import array

# Arrays são pra listas ENORMES (mais de mil itens ou coisas por ai). Ela ta entre tuples e listas no quesito memória, então é bem útil saber usar, melhora bastante a 
#performance, ah e ela é mutable, ou seja, pode ser modificada, adicionar ou remover itens e etc; Igual a uma lista mesmo só que maior e gastando menos, e mutable.

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])   # Transformou a lista em array, o 'u' é o tipo da lista, nesse caso string 
numeros_i = array('i', [10, 20, 30, 40])    # Aqui o 'i' representa o tipo int
numeros_f = array('f', [1.2, 2.2, 3.2])     # Aqui 'f' é de float
                                            # Todos esses tipos estão na documentação da array, mas basicamente esses devem ser os que eu mais vou usar
print(letras)
print(numeros_i)
print(numeros_f)