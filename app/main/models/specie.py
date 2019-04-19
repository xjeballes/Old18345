from .. import db
from app.main.models import breed

class Specie(db.Model):
    __tablename__ = "specie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    specie_name = db.Column(db.String(100), unique=True, nullable=False)

    has_breeds = db.relationship("Breed", backref="specie", lazy=True)
    
    def __repr__(self):
        return "<specie '{}'>".format(self.specie_name)