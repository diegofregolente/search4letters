from vsearch import search4letters

phrase = "Don't panic!"
plist = list(phrase)
print(plist)

new_phrase = ''.join(plist[1:3]) # Ignora o D e pega "on"
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]]) # junta o "on" com os indixes espaço, T, a, p.

print(plist)
print(new_phrase)

letras = search4letters(phrase, 'Dont')

print(f'Em {phrase} temos as letras {letras}')