class Pessoa:

    def __init__(self, nome, telefone, ):
        self.__nome = nome
        self.__telefone = telefone

    def mostraDados(self):
        return(f' Nome: {self.__nome}, Telefone: {self.__telefone}')


pessoa = Pessoa('Suelen', '51 32345443')
print(pessoa.mostraDados())

# acessando atributo privado
print(pessoa._Pessoa__nome)
