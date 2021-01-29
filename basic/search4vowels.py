def search4vowels(phrase:str) -> set: # Informando ao usuário que deve retornar um conjunto no fim
    """
    Função que procura vogais em palavras 
    :param phrase:str palavra provida para procurar vogais
    :return: retorna a inserseção de vowels com word
    """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


help(search4vowels)
print(search4vowels(str(input('Provide a word to search vowels: ')).lower()))
