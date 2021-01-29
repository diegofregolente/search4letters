vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Provenha uma palavra para procurar as vogais: '))
found = []

for letra in palavra:
    letra = letra.lower()
    if letra in vogais:
        if letra not in found:
            found.append(letra)

for vogais in found:
    print(vogais)

if len(found) > 0:
    print(f'{palavra} tem vogal')
else:
    print(f'{palavra} não tem vogal')