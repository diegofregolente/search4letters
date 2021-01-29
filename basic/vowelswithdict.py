palavra = str(input('Digite uma palavra: ')).lower().strip()
vogais = ['a', 'e', 'i', 'o', 'u']

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letra in palavra:
    if letra in vogais:
        found[letra] += 1
for k, v in sorted(found.items()):
    print(f'{k} foi encontrado {v} vezes.')