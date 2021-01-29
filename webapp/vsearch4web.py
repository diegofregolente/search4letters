from flask import Flask, render_template, request, escape, session, copy_current_request_context
from vsearch import search4letters
from checker import check_logged_in
from DBcm import UseDataBase, ConnectionErro, CredentialsError, SQLError
from threading import Thread
from time import sleep

app = Flask(__name__)  # start

app.config['dbconfig'] = dict(host='127.0.0.1', user='root', password='123', database='vsearchlogDB')  # credentials


@app.route('/login')  # login to view pages
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')  # logout to not view pages
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are now logged out'


@app.route("/search4", methods=['POST', 'GET'])  # recebe o form do HTML
def do_search() -> 'html':
    @copy_current_request_context  # salva os dados do request
    def log_request(req: 'flask_request', res: str) -> None:  # recebe request / search4letters
        sleep(15)  # atrasa o código pra não gerar atrasos
        with UseDataBase(app.config['dbconfig']) as cursor:  # utiliza o interpretador do MySQL
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as erro:
        print('***** Logging failed with this error:', str(erro))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')  # pagina onde será inserido os forms.
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route("/viewlog")  # tabela sincronizada com MySQL para ver todas as pesquisas
@check_logged_in
def viewlog_page() -> 'html':
    try:
        with UseDataBase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_Addr', 'User_Agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_title=titles,
                               the_data=contents, )
    except ConnectionErro as err:
        print('Sua database mudou? Erro:', str(err))
    except CredentialsError as err:
        print('User-id/Password estão incorretos, Error:', str(err))
    except SQLError as err:
        print('Algo deu errado:', str(err))
    except Exception as erro:
        print('Algo deu errado:', str(erro))
    return 'Error'


app.secret_key = '123'

if __name__ == '__main__':
    app.run(debug=True)
