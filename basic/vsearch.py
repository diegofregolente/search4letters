def search4vowels(phrase: str) -> set: # Informando ao usuário que deve retornar um conjunto no fim
    """
    Função que procura vogais em palavras
    :param phrase:str palavra provida para procurar vogais
    :return: retorna a inserseção de vowels com word
    """
    return set('aeiou').intersection(set(phrase.lower()))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    Função que recebe uma frase e uma sequencia de letras (opcional) padrão vogais.
    :param phrase: Frase em string
    :param letters:Letras em string ou se vazio recebe aeiou
    :return:Converte phrase/letters em conjunto e lower, após verifica as semelhanças e adiciona a um conjunto
    """
    return set(letters.lower()).intersection(set(phrase.lower()))
