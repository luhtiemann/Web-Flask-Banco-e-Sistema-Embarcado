from models.db import db

class Compra(db.Model):
    __tablename__ = "compra"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    fl_concluido = db.Column(db.Boolean)

    def get_compras():
        compras = Compra.query\
                    .add_columns(Compra.id, Compra.fl_concluido).all()
    
        return compras
    
    def save_compra(fl_concluido):
    
        compra = Compra(fl_concluido=fl_concluido)
        
        db.session.add(compra)
        db.session.commit()
