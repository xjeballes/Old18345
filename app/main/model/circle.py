from .. import db


class Circle(db.Model):
    __tablename__ = "circle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    contact_num = db.Column(db.String(20), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    circle_name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<circle '{}'>".format(self.group_name)
