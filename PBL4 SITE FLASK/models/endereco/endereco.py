from models.db import db
from models import Conta

class Endereco(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    #conta_id = db.Column(db.Integer, db.ForeignKey(Conta.id))
    rua = db.Column(db.String(200))
    estado = db.Column(db.String(30))
    cidade = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    complemento = db.Column(db.String(100))
    cep = db.Column(db.String(9))


    def get_enderecos():
        enderecos = Endereco.query\
                    .add_columns(Endereco.id, Endereco.rua, Endereco.estado, Endereco.cidade, Endereco.bairro, Endereco.numero, Endereco.complemento, Endereco.cep).all()
    
        return enderecos
    
    def save_endereco(rua, estado, cidade, bairro, numero, complemento, cep):
    
        endereco = Endereco(rua=rua, estado=estado, cidade=cidade, bairro=bairro, numero=numero, complemento=complemento, cep=cep)
        
        db.session.add(endereco)
        db.session.commit()

    def delete_endereco(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_endereco_by_id(cls, endereco_id):
        return cls.query.get(endereco_id)
    
    def update_endereco(self, rua, estado, cidade, bairro, numero, complemento, cep):
        self.rua = rua
        self.estado = estado
        self.cidade = cidade
        self.bairro= bairro
        self.numero= numero
        self.complemento= complemento
        self.cep= cep

        db.session.commit()
