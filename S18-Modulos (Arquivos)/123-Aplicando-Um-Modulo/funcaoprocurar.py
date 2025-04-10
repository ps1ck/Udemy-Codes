def find_index(lista, itemProcurado):
    for index, valorLista in enumerate(lista):   # enumerate retorna o index e o valor de cada item da lista. então ele gera i=0, valor='a' e assim por diante.
        if valorLista == itemProcurado:
            return index
    return "Não está na lista"
