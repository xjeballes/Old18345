from .. import db
from app.main.models import pet_specie_rel

class Pet(db.Model):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    pet_name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    specie_rel = db.relationship("specie", secondary=pet_specie_rel, backref=db.backref("pet", lazy=True))

    def __repr__(self):
        return "<pet '{}'>".format(self.pet_name)
