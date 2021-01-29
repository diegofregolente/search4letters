palavra = "garrafas" # definindo variavel
for cerveja_num in range(20, 0, -1): # loop para contar cervejas
    print(cerveja_num, palavra, "cervejas na parede.") # mostre a mensagem n da cerveja, garrafas na parede.
    print("Pegue uma.")
    print("Passe adiante.")
    if cerveja_num == 1: # se chegar na ultima mostre que não tem mais cerveja
        print("Não tem mais cervejas na parede.")
    else: # se não
        cerveja_num -= 1 # reduza o valor do total de cerveja
        if cerveja_num == 1: # se reduzir para 1 tire do plural
            palavra = "garrafa"
        print(cerveja_num, palavra, "de cerveja na parede.") # então mostre a mensagem.
    print() # pule uma linha para a proxima execução do for
