from datetime import datetime
from random import randint
from time import sleep, strftime

impares = [
        1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59
        ]

for i in range(5):
    minuto_atual = datetime.today().minute

    if minuto_atual in impares:
        print('This minute is impar')
    else:
        print('This minute is par')

    dia_da_semana = strftime("%A")

    print(f'Today is a {dia_da_semana}')

    if dia_da_semana == 'Saturday':
        print('Party!!')
    elif dia_da_semana == "Sunday":
        print('Recover.')
    else:
        print('Work, Work, Work.')
    print()
    sleep(randint(1, 60))
