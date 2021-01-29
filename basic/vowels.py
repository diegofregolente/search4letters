vowels2 = set('aeiiiouuu')
word = input('Provide a word to search for vowels:').lower()
found = vowels2.intersection(set(word))
for v in found:
    print(v)