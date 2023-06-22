from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from models import Conta
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint("auth", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/login_post', methods=['POST'])
def login_post():  
    email = request.form.get('email')
    senha = request.form.get('senha')
    remember = True if request.form.get('remember') else False

    conta = Conta.query.filter_by(email=email).first()
    if not conta or not check_password_hash(conta.senha, senha): 
        flash('Email ou senha errados, tente novamente.')
        return redirect(url_for('auth.login'))

    login_user(conta, remember=remember)
    return redirect(url_for('admin.admin_index'))

@auth.route('/signup')
def signup():
    return render_template("auth/signup.html")

@auth.route('/signup_post', methods=['POST'])
def signup_post():
    if request.method == 'POST':
        nome = request.form.get('nome', None)        
        usuario = request.form.get('usuario', None)
        email = request.form.get('email', None)
        senha = request.form.get('senha', None)
        senha = generate_password_hash(senha)

        Conta.save_conta(nome, usuario, email, senha)
        return redirect('login')

    return redirect(url_for('auth.login'))


#parte do joao verificar login e tipo de usuario