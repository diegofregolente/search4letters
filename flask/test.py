from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Hello Friend, Welcome back!<h1>'


@app.route("/<name>")
def page(name):
    return f'<h1> Hello {name}, Welcome back!<h1>'


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()



