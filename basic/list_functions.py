frase = "Fuck society, hello friend."
lista = list(frase)

print(lista)

for r in range(13):
    lista.pop()

lista.remove(",")
lista.remove(' ')
lista.pop()
lista.extend("Fuck")
for r in range(4):
    lista.pop(0)

lista.insert(7, ' ')

nova_frase = ''.join(lista).upper()
print(nova_frase)
print(lista)
