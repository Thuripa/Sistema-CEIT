from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>Saindo...</p>'


@auth.route('/cadastro')
def sign_up():
    return render_template('cadastro.html')
