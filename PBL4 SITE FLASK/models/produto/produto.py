from models.db import db

class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    valor = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    dt_fabricacao = db.Column(db.Date)


    def get_produtos():
        produtos = Produto.query\
                    .add_columns(Produto.valor, Produto.quantidade, Produto.dt_fabricacao).all()

        return produtos
    
    def save_produto(valor, quantidade, dt_fabricacao):
    
        produto = Produto(valor=valor, quantidade=quantidade, dt_fabricacao=dt_fabricacao)
        
        db.session.add(produto)
        db.session.commit()