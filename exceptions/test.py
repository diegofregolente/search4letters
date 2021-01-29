# import sys

# try:
#     with open('texto.txt') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('Não existe o arquivo texto.txt....')
# except PermissionError:
#     print('Você não tem permissão pra ver esse arquivo.')
# except:
#     print('Algum erro foi encontrado, infelizmente não será possível abrir esse arquivo.')

# try:
#     1/0
# except:
#     erro = sys.exc_info()
#     for e in erro:
#         print(e)

# try:
#     print(a)
# except Exception as erro:
#     print('Algum outro erro foi identificado:', str(erro))

# class ConnectionErro(Exception):
#     pass
#
# try:
#     raise ConnectionErro('BAD, VERY BAD.')
# except ConnectionErro as err:
#     print('Got:', str(err))


try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('This is not allowed.')
except Exception as error:
    print('Some other error occured:', str(error))
