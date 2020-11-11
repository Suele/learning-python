"""
    Escreva código para fazer uma função que retorne a primeira palavra em um texto.
    Se seu código estiver certo ao rodar a célula vc reverá receber 'Exemplo: Hello' como output
"""


def first_word(text: str) -> str:
    text = text.lstrip().replace(',', ' ')
    if text.split()[0] == '...':
        return text.split()[1]
    elif text.split()[0].__contains__('.'):
        text = text.replace('.', ' ')
        return text.split()[0]
    else:
        return text.split()[0]


#print(first_word("Hello world"))
#print(first_word(" a word "))
#print(first_word("... and so on ..."))
print(first_word("greetings, friends"))
# print(first_word("Hello.World"))
