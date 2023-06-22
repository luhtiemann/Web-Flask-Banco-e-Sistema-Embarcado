from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Compra

compra = Blueprint("compra", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@compra.route("/")
def compra_index():
    return render_template("/compra/compra_index.html")

@compra.route("/register_compra")
def register_compra():
    return render_template("/compra/register_compra.html")

@compra.route("/view_compra")
def view_compra():
    compras = Compra.get_compras()
    return render_template("/compra/view_compra.html", compras = compras)

@compra.route("/save_compra", methods = ["POST"])
def save_compras():
    peso = request.form.get("peso")
    dt_fabricacao = request.form.get("dt_fabricacao")

    Compra.save_compra(peso, dt_fabricacao)

    return redirect(url_for('admin.compra.view_compra'))