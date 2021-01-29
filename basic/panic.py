phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop() # remove os ultimos quatro nic!
plist.pop(0) # remove o D
plist.remove("'") # remove o '
plist.extend([plist.pop(), plist.pop()]) # remove o ultimo e adiciona de novo, e remove o penultimo e adiciona de novo
plist.insert(2, plist.pop(3)) # remove o 3 e coloca no lugar do 2


new_phrase = ''.join(plist) # junta os espaços e recebe o novo valor de plistpanic.py
print(plist)
print(new_phrase)