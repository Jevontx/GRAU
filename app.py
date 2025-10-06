from flask import Flask, render_template, request, redirect, url_for, session, flash
from controller import cadastrar_freelancer, listar, buscar, remover, ocupar, liberar, manager
import os

app = Flask(__name__)
app.secret_key = 'dev_secret_key'  # Trocar em produção

# Simple demo user
USERS = {
    "jevon": "692991"
}

@app.route('/')
def home():
    if not session.get("user"):
        return redirect(url_for('login'))
    term = request.args.get("q", "")
    if term:
        results = buscar(term)
    else:
        results = listar()
    return render_template("index.html", freelancers=results, q=term, user=session.get("user"))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get("username")
        pwd = request.form.get("password")
        if USERS.get(user) == pwd:
            session["user"] = user
            return redirect(url_for('home'))
        flash("Credenciais inválidas", "danger")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add():
    if not session.get("user"):
        return redirect(url_for('login'))
    data = {
        "id": request.form.get("id"),
        "nome": request.form.get("nome"),
        "idade": request.form.get("idade"),
        "categoria": request.form.get("categoria"),
        "cargo": request.form.get("cargo"),
        "valor_hora": request.form.get("valor_hora"),
        "disponibilidade": request.form.get("disponibilidade"),
        "fornecedor": request.form.get("fornecedor")
    }
    try:
        cadastrar_freelancer(data)
        flash("Freelancer cadastrado com sucesso", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for('home'))

@app.route('/remove/<id>')
def remove_route(id):
    if not session.get("user"):
        return redirect(url_for('login'))
    remover(id)
    flash("Removido", "info")
    return redirect(url_for('home'))

@app.route('/ocupar/<id>')
def ocupar_route(id):
    if not session.get("user"):
        return redirect(url_for('login'))
    ocupar(id)
    flash("Marcado como ocupado", "info")
    return redirect(url_for('home'))

@app.route('/liberar/<id>')
def liberar_route(id):
    if not session.get("user"):
        return redirect(url_for('login'))
    liberar(id)
    flash("Marcado como disponível", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
