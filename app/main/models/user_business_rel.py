from .. import db

user_business_rel = db.Table("user_business_rel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("business_id", db.Integer, db.ForeignKey("business.id"))
)