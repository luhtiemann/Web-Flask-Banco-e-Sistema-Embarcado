from models.db import db

class Pote(db.Model):
    __tablename__ = "pote"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    peso = db.Column(db.Float)
    dt_fabricacao = db.Column(db.DateTime)

    def get_pote():
        pote = Pote.query\
                    .add_columns(Pote.id, Pote.peso, Pote.dt_fabricacao).all()
        return pote
    
    def save_pote(peso, dt_fabricacao):
    
        pote = Pote(peso=peso, dt_fabricacao=dt_fabricacao)
        
        db.session.add(pote)
        db.session.commit()