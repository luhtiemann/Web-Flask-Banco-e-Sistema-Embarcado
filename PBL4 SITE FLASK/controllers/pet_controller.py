from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Pet

pet = Blueprint("pet", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@pet.route("/")
def pet_index():
    return render_template("/pet/pet_index.html")

@pet.route("/register_pet")
def register_pet():
    return render_template("/pet/register_pet.html")

@pet.route("/view_pet")
def view_pet():
    pets = Pet.get_pets()
    return render_template("/pet/view_pet.html", pets = pets)

@pet.route("/save_pet", methods = ["POST"])
def save_pets():
    nome = request.form.get("nome")
    raca = request.form.get("raca")
    idade = request.form.get("idade")
    tipo = request.form.get("tipo")


    Pet.save_pet(nome, raca, idade, tipo)

    return redirect(url_for('admin.pet.view_pet'))

@pet.route('/delete_pet/<int:pet_id>', methods=['GET', 'POST'])
def delete_pet(pet_id):
    pet_del = Pet.get_pet_by_id(pet_id)
    if pet_del:
        pet_del.delete_pet()
        flash('Employee deleted successfully!')
    else:
        flash('Employee not found!')
    return redirect(url_for('admin.pet.view_pet'))

@pet.route("/edit_pet/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet_upt = Pet.query.get(pet_id)

    if request.method == "POST":
        novo_nome = request.form.get("novo_nome")
        novo_raca = request.form.get("novo_raca")
        novo_idade = request.form.get("novo_idade")
        novo_tipo = request.form.get("novo_tipo")

        pet_upt.update_pet(novo_nome, novo_raca, novo_idade, novo_tipo)

        return redirect(url_for("admin.pet.view_pet"))
    else:
        return render_template("/pet/edit_pet.html", pet_upt=pet_upt)