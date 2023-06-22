from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Dispenser

dispenser = Blueprint("dispenser", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@dispenser.route("/")
def dispenser_index():
    return render_template("/dispenser/dispenser_index.html")

@dispenser.route("/register_dispenser")
def register_dispenser():
    return render_template("/dispenser/register_dispenser.html")

@dispenser.route("/view_dispenser")
def view_dispenser():
    dispensers = Dispenser.get_dispenser()
    return render_template("/dispenser/view_dispenser.html", dispensers = dispensers)

@dispenser.route("/save_dispenser", methods = ["POST"])
def save_dispensers():
    peso = request.form.get("peso")
    dt_fabricacao = request.form.get("dt_fabricacao")

    Dispenser.save_dispenser(peso, dt_fabricacao)

    return redirect(url_for('admin.dispenser.view_dispenser'))