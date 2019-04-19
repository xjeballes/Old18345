from .. import db

user_circle_rel = db.Table("user_circle_rel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("circle_id", db.Integer, db.ForeignKey("circle.id"))
)