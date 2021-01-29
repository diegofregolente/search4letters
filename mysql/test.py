import mysql.connector


dbconfig = { 'host': '127.0.0.1',
             'user': 'bruceqqqqq',
             'password': '123',
             'database': 'vsearchlogDB', }

conn = mysql.connector.connect(**dbconfig) # conecta ao banco de dados atraves do dicionario criado
cursor = conn.cursor() # cria um cursor para enviar dados ao mysql
# _SQL = """show tables""" mostra quais tabelas estão dentro do DB
# _SQL = """describe log""" mostra quais os campos da tabela criada como log
# # res = cursor.fetchall recupera todas as linhas que compoem os resultados, fetchmany recupero a linha especificada, fetchone recupera uma linha
_SQL = """Insert into log
        (phrase, letters, ip, browser_String, results)
        values
        (%s, %s, %s, %s, %s)""" # Insere na table log esses campos.
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Google Chrome', 'set()')) # de acordo com _SQL acima adiciona as strings formadas aqui e inserete no _SQL
conn.commit() # grava na memoria do DB
_SQL = """select * from log""" # Mostra todas as linhas de log
cursor.execute(_SQL) # executa a função
for row in cursor.fetchall(): # faz um loop para mostra um em cada linha
    print(row)
cursor.close()
conn.close()
