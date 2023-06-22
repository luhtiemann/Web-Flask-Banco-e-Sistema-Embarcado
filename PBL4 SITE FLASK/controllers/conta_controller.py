from flask import Blueprint, render_template,redirect,url_for, request
from models import Conta

conta = Blueprint("conta", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@conta.route("/")
def conta_index():
    return render_template("/conta/conta_index.html")


@conta.route("/view_conta")
def view_conta():
    contas = Conta.get_contas()
    return render_template("/conta/view_conta.html", contas = contas)


@conta.route("/save_conta", methods = ["POST"])
def save_contas():
    nome = request.form.get("nome")
    sobrenome = request.form.get("sobrenome")
    usuario = request.form.get("usuario")
    email = request.form.get("email")
    senha = request.form.get("senha")

    Conta.save_conta(nome, sobrenome, usuario, email, senha)

    return redirect(url_for('admin.conta.view_conta'))

@conta.route("/edit/<int:contas_id>", methods=["GET", "POST"])
def edit_conta(contas_id):
    conta_upt = Conta.query.get(contas_id)

    if request.method == "POST":
        novo_nome = request.form.get("novo_nome")
        novo_usuario = request.form.get("novo_usuario")
        novo_email = request.form.get("novo_email")
        novo_senha = request.form.get("novo_senha")

        conta_upt.update_conta(novo_nome, novo_usuario, novo_email, novo_senha)

        return redirect(url_for("admin.conta.view_conta"))
    else:
        return render_template("/conta/edit.html", conta_upt=conta_upt)