from flask import request, render_template, redirect, url_for
from models.db import db
from flask_login import UserMixin

class Conta(UserMixin, db.Model):
    __tablename__ = "conta"
    id = db.Column("id",  db.Integer(), primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=False)
    usuario = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    senha = db.Column(db.String(1024), nullable=False) 

    def save_conta(nome, usuario, email, senha):
    
        conta = Conta(nome=nome, usuario=usuario, email=email, senha=senha)
        
        db.session.add(conta)
        db.session.commit()

    def get_contas():
        contas = Conta.query\
                    .add_columns(Conta.id, Conta.nome, Conta.usuario, Conta.email, Conta.senha).all()
    
        return contas
    

    def update_conta(self, nome, usuario, email, senha):
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha

        db.session.commit()


"""
    roles = db.relationship("Role", back_populates="contas", secondary="user_roles")
    reads = db.relationship("Read", backref="contas", lazy=True)    
"""




        