from flask import Blueprint, render_template,redirect,url_for, request
from models import Produto

produto = Blueprint("produto", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@produto.route("/")
def produtos_index():
    return render_template("/produto/produto_index.html")

@produto.route("/register_produto")
def register_produto():
    return render_template("/produto/register_produto.html")

@produto.route("/view_produto")
def view_produto():
    produtos = Produto.get_produtos()
    return render_template("/produto/view_produto.html", produtos = produtos)

@produto.route("/save_produto", methods = ["POST"])
def save_produtos():
    preco = request.form.get("preco")
    quantidade = request.form.get("quantidade")
    qnt_disponivel = request.form.get("qnt_disponivel")

    Produto.save_produto(preco, quantidade, qnt_disponivel)

    return redirect(url_for('admin.pagamento.register_pagamento'))