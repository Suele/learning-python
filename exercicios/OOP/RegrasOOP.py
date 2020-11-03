"""
Atributos - podem ser públicos ou privados, representam caracteristicas dos objetos.
Tem atributos de instancia, classe e dinamicos.

Atributos de instancia sao declarados dentro do construtor e cada instancia da classe tem
os seus atributos, ou seja cada instancia terá atributos diferentes.

Atributos privados são iniciados com __undescord. Isso é uma convensão.

Para ter acesso fora da classe de atributos privados usa-se
print(pessoa._Pessoa__nome) -> nomeDaInstancia da classe + nomeDaClasse + o atributoPrivado

Atributos da classe => são atributos que são declarados na classe e todas as instancias desta classe teram
o mesmo valor do atributo.

Atributos dinamicos => são criados em tempo de execucao.
OBS: atributos dinamicos e de instancia podem ser excluidos da instancia que os criou.
"""


class Pessoa:

    def __init__(self, nome, telefone, ):
      # atributos privados só devem ser acessados pela classe
        self.__nome = nome
        self.__telefone = telefone


# instancia da classe Pessoa
pessoa = Pessoa('Suelen', '51 32345443')

# acessando atributo privado
print(pessoa._Pessoa__nome)


class Produto:
  # atributo da classe todas as instancias
  # da classe teram o mesmo valor.
    imposto = 0.05

    def __init__(self, nome, descricao, valor):
      # atributos de instancia todas as instancias
      # da classe teram valores diferentes.
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


p1 = Produto('arroz', 'tipo 1', 3.90)

# esse atributo não existe na classe produto.
# atributo dinamico
p1.quantidade = 1

print(f'Nome: {p1.nome}, Descricao: {p1.descricao}, Valor: {p1.valor}, Quantidade: {p1.quantidade}')

# é um dicionario mostra os dados atribuidos em chave e valor.
print(p1.__dict__)
