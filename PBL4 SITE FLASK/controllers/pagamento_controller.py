from flask import Blueprint, render_template,redirect,url_for, request
from models import Pagamento
pagamento = Blueprint("pagamento", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@pagamento.route("/")
def pagamento_index():
    return render_template("/pagamento/pagamento_index.html")


@pagamento.route("/register_pagamento")
def register_pagamento():
    return render_template("/pagamento/register_pagamento.html")

@pagamento.route("/view_pagamentos")
def view_pagamentos():
    pagamentos = Pagamento.get_pagamento()
    return render_template("/pagamento/view_pagamentos.html", pagamentos = pagamentos)

@pagamento.route("/save_pagamentos", methods = ["POST"])
def save_pagamentos():
    quantidade = request.form.get("quantidade")
    valor_total = request.form.get("valor_total")
    tipo = request.form.get("tipo")
    nome = request.form.get("nome")
    cvc = request.form.get("cvc")
    dt_vencimento = request.form.get("dt_vencimento")
    numero = request.form.get("numero")

    Pagamento.save_pagamento(quantidade, valor_total, tipo, nome, cvc, dt_vencimento, numero)

    return redirect(url_for('admin.pagamento.view_pagamentos'))


