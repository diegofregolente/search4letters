def double(arg):
    print('Before: ', arg)
    arg = arg * 2 # Strings, Inteiros e as Tuplas só mudam dentro da função, após isso volta
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data') # Listas, Conjunto e Dicionarios mudam no programa principal
    print('After: ', arg)

double(1)
change([1])
