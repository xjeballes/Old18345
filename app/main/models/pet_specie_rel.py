from .. import db

pet_specie_rel = db.Table("pet_specie_rel",
    db.Column("pet_id", db.Integer, db.ForeignKey("pet.id")),
    db.Column("specie_id", db.Integer, db.ForeignKey("specie.id"))
)