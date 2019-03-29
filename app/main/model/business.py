from .. import db

class Business(db.Model):
    __tablename__ = "business"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_num = db.Column(db.String(20), nullable=True)
    business_name = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<business '{}'>".format(self.business_name)