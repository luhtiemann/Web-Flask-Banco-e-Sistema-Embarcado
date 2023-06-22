from models.db import db

class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column("id",  db.Integer(), primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=False)
    raca = db.Column(db.String(30), nullable=False, unique=False)
    idade = db.Column(db.Integer, nullable=False, unique=False)
    tipo = db.Column(db.String(30), nullable=False, unique=False)

    def get_pets():
        pets = Pet.query\
                    .add_columns(Pet.id, Pet.nome, Pet.raca, Pet.idade, Pet.tipo).all()
    
        return pets
    
    def save_pet(nome, raca, idade, tipo):
    
        pet = Pet(nome=nome, raca=raca, idade=idade, tipo=tipo)
        
        db.session.add(pet)
        db.session.commit()

    def delete_pet(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_pet_by_id(cls, pet_id):
        return cls.query.get(pet_id)
    
    def update_pet(self, nome, raca, idade, tipo):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.tipo = tipo

        db.session.commit()