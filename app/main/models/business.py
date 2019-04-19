from .. import db

class Business(db.Model):
    __tablename__ = "business"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(20), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<business '{}'>".format(self.business_name)