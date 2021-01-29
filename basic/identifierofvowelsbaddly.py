palavras = ['Diego', 'Anel']
contador = 0
vogais = ''

for palavra in palavras:
    for letra in palavra:
        if letra in "aeiouAEIOU":
            contador += 1
            vogais += letra
    if contador > 1:
        print(f'{palavra} tem vogal e elas são {vogais}.')
    else:
        print(f'{palavra} não tem vogal')
    contador = 0
    vogais = ''