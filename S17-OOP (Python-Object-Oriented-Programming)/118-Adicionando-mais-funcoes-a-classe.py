class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):       
        self.nome = nome                                        
        self.sobrenome = sobrenome                              
        self.data_nascimento = data_nascimento

    def nome_completo(self):                                # Criamos uma função dentro da classe, usamos o self para o objeto que será trocado, aqui não foi necessário
        return self.nome + ' ' + self.sobrenome             #escrever de novo nome, sobrenome.. por que eles já foram mostrados na função de cima. Então é só escrever a
                                                            #função em si, no caso aqui o objetivo é escrever o nome completo atraves de uma função.
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')        
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')         
usuario3 = Funcionarios('Andre', 'Iacono', '11/03/2003')

print(usuario1.nome + ' ' + usuario1.sobrenome)             # Todas as 3 dão o mesmo resultado, a primeira é o jeito "manual", segundo e terceiro é usando a função que   
print(usuario1.nome_completo())                             #criamos, mas a primeira chama o objeto e logo depois a função, já a terceira chama a classe-objeto-função,
print(Funcionarios.nome_completo(usuario1))                 #que na minha opinião e também do professor, faz mais sentido, mas tanto a 2° quanto a 3° funcionam.