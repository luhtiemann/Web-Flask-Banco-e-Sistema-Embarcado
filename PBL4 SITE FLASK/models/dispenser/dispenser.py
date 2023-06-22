from models.db import db

class Dispenser(db.Model):
    __tablename__ = "dispenser"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    peso = db.Column(db.Float)
    dt_fabricacao = db.Column(db.DateTime)

    def get_dispenser():
        dispenser = Dispenser.query\
                    .add_columns(Dispenser.id, Dispenser.peso, Dispenser.dt_fabricacao).all()
        return dispenser
    
    def save_dispenser(peso, dt_fabricacao):
    
        dispenser = Dispenser(peso=peso, dt_fabricacao=dt_fabricacao)
        
        db.session.add(dispenser)
        db.session.commit()

        