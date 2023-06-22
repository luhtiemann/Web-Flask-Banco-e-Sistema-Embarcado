from models.db import db

class Pagamento(db.Model):
    __tablename__ = "pagamento"
    id = db.Column("id",  db.Integer(), primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False, unique=False)
    valor_total = db.Column(db.Float, nullable=False, unique=False)
    tipo = db.Column(db.String(30), nullable=False, unique=False)
    nome = db.Column(db.String(50), unique=False)
    cvc = db.Column(db.Integer(), unique=False)
    dt_vencimento = db.Column(db.Date, unique=False)
    numero = db.Column(db.BIGINT(), unique=False)


    def get_pagamento():
        pagamento = Pagamento.query\
                    .add_columns(Pagamento.id, Pagamento.quantidade, Pagamento.valor_total, Pagamento.tipo, Pagamento.nome, Pagamento.cvc, Pagamento.dt_vencimento, Pagamento.numero).all()
        return pagamento
    
    def save_pagamento(quantidade, valor_total, tipo, nome, cvc, dt_vencimento, numero):
    
        pagamento = Pagamento(quantidade=quantidade, valor_total=valor_total, tipo=tipo, nome=nome, cvc=cvc, dt_vencimento=dt_vencimento, numero=numero)
        
        db.session.add(pagamento)
        db.session.commit()