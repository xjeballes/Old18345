from .. import db

class Circle(db.Model):
    __tablename__ = "circle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    circle_name = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<circle '{}'>".format(self.circle_name)
