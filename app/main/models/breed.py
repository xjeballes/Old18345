from .. import db

class Breed(db.Model):
    __tablename__ = "breed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    breed_name = db.Column(db.String(100), unique=True)

    specie_id = db.Column(db.Integer, db.ForeignKey("specie.id"), nullable=False)

    def __repr__(self):
        return "<breed '{}'>".format(self.breed_name)