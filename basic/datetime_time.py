import datetime
import time
print(datetime.date.today()) # mostra a data de hoje
print(datetime.date.today().day) # mostra o dia de hoje
print(datetime.date.today().month) # mostra o mes de hoje
print(datetime.date.today().year) # mostra o ano de hoje
print(datetime.date.isoformat(datetime.date.today())) # data de hoje como uma string
print(time.strftime("%H:%M")) # mostra a hora atual
print(time.strftime("%A:%p")) # mostra o dia da semana e se é AM (manhã/madrugada) ou PM(tarde/noite)