"""
Você recebe os preços atuais das ações em forma de dicionário onde o código identificador do mercado é uma chave e o valor é o preço da ação. 
Você tem que descobrir quais ações custam mais e retornar o código identificador de mercado (símbolo de ação) como uma string.
"""


def best_stock(data):
    acaoComMaiorValor = max(data, key=lambda chave: float(data[chave]))
    return acaoComMaiorValor


print("Example:")
print(best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}))

print(
    best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    })
)

print(
    best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    })
)
