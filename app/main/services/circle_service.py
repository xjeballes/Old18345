import uuid
import datetime

from app.main import db
from app.main.models.circle import Circle


def create_new_circle(data):
    circle = Circle.query.filter_by(email=data['email']).first()
    if not circle:
        new_circle = Circle(
            circle_name=str(uuid.uuid4()),
            email=data['email'],
            contact_num=data['contact_num'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_circle)
        response_object = {
            'status': 'success',
            'message': 'circle created'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'This circle already exists.',
        }
        return response_object, 409


def get_all_circle():
    return Circle.query.all()


def get_circle(circle_name):
    return Circle.query.filter_by(circle_name=circle_name).first()


def delete_circle(circle_name):
    db.session.delete(circle_name)
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
