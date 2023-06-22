from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Endereco

endereco = Blueprint("endereco", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@endereco.route("/")
def endereco_index():
    return render_template("/endereco/endereco_index.html")

@endereco.route("/register_endereco")
def register_endereco():
    return render_template("/endereco/register_endereco.html")

@endereco.route("/view_endereco")
def view_endereco():
    enderecos = Endereco.get_enderecos()
    return render_template("/endereco/view_endereco.html", enderecos = enderecos)

@endereco.route("/save_endereco", methods = ["POST"])
def save_enderecos():
    rua = request.form.get("rua")
    estado = request.form.get("estado")
    cidade = request.form.get("cidade")
    bairro = request.form.get("bairro")
    numero = request.form.get("numero")
    complemento = request.form.get("complemento")
    cep = request.form.get("cep")

    Endereco.save_endereco(rua, estado, cidade, bairro, numero, complemento, cep)

    return redirect(url_for('admin.endereco.view_endereco'))

@endereco.route('/delete_endereco/<int:endereco_id>', methods=['GET', 'POST'])
def delete_endereco(endereco_id):
    endereco_del = Endereco.get_endereco_by_id(endereco_id)
    if endereco_del:
        endereco_del.delete_endereco()
        flash('Employee deleted successfully!')
    else:
        flash('Employee not found!')
    return redirect(url_for('admin.endereco.view_endereco'))

@endereco.route("/edit_endereco/<int:endereco_id>", methods=["GET", "POST"])
def edit_endereco(endereco_id):
    endereco_upt = Endereco.query.get(endereco_id)

    if request.method == "POST":
        novo_rua = request.form.get("novo_rua")
        novo_estado = request.form.get("novo_estado")
        novo_cidade = request.form.get("novo_cidade")
        novo_bairro = request.form.get("novo_bairro")
        novo_numero = request.form.get("novo_numero")
        novo_complemento = request.form.get("novo_complemento")
        novo_cep = request.form.get("novo_cep")

        endereco_upt.update_endereco(novo_rua, novo_estado, novo_cidade, novo_bairro, novo_numero, novo_complemento, novo_cep)

        return redirect(url_for("admin.endereco.view_endereco"))
    else:
        return render_template("/endereco/edit_endereco.html", endereco_upt=endereco_upt)