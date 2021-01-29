# todos = open('todos.txt', 'a')
#
# print('Put out the trash.', file=todos)
# print('Feed the cat.', file=todos)
# print('Prepare tax return.', file=todos)
#
# todos.close()


with open('todos.txt', 'r') as tasks:
    for chore in tasks:
        print(chore, end='')

# 'r' Abre um arquivo para leitura = read
# 'w' Abre um arquivo para gravação, se o arquivo tiver dadosm esvazia o arquivo com os dados antes de continuar
# 'a' Abre um arquivo para anexação, preserva o contéudo do arquivo
# 'x' Abre um novo arquivo para a gravação, Falha se o arquivo já existir
