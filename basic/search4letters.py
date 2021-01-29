def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """
    Função que recebe uma frase e uma sequencia de letras (opcional) padrão vogais.
    :param phrase: Frase em string
    :param letters:Letras em string ou se vazio recebe aeiou
    :return:Converte phrase/letters em conjunto e lower, após verifica as semelhanças e adiciona a um conjunto
    """
    return set(letters.lower()).intersection(set(phrase.lower()))


print(search4letters('GALAXY', 'xyz'))
print(search4letters('I Love Amanda'))
