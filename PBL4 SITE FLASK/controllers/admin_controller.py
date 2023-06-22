from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user, login_required
from controllers.conta_controller import conta
from controllers.produto_controller import produto
from controllers.dispenser_controller import dispenser
#from controllers.pote_controller import pote
from controllers.pet_controller import pet
from controllers.pagamento_controller import pagamento
from controllers.endereco_controller import endereco
from controllers.compra_controller import compra

admin = Blueprint("admin", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

admin.register_blueprint(conta, url_prefix='/conta')
admin.register_blueprint(produto, url_prefix='/produto')
admin.register_blueprint(dispenser, url_prefix='/dispenser')
#admin.register_blueprint(pote, url_prefix='/pote')
admin.register_blueprint(pet, url_prefix='/pet')
admin.register_blueprint(pagamento, url_prefix='/pagamento')
admin.register_blueprint(endereco, url_prefix='/endereco')
admin.register_blueprint(compra, url_prefix='/compra')

@admin.route("/")
@admin.route("/admin")
@login_required
def admin_index():

    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    else:
        return render_template("/admin/admin_index.html", nome = current_user.nome)

    
#trocar tudo de ticket para order, conferir se n vai entrar em conflito com outro nome order