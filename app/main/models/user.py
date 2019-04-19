from .. import db, flask_bcrypt
from app.main.models import business, circle

user_business_rel = db.Table("user_business_rel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("business_id", db.Integer, db.ForeignKey("business.id"))
)

user_circle_rel = db.Table("user_circle_rel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("circle_id", db.Integer, db.ForeignKey("circle.id"))
)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    contact_no = db.Column(db.String(20), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    
    has_pets = db.relationship("Pet", backref="user", lazy=True)
    
    business_rel = db.relationship("Business", secondary=user_business_rel, backref=db.backref("user", lazy=True))
    circle_rel = db.relationship("Circle", secondary=user_circle_rel, backref=db.backref("user", lazy=True))

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
