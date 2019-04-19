import uuid
import datetime

from app.main import db
from app.main.models.business import Business


def create_new_business(data):
    business = Business.query.filter_by(email=data['email']).first()
    if not business:
        new_business = Business(
            business_name=str(uuid.uuid4()),
            email=data['email'],
            contact_num=data['contact_num'],
            address=data['address'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_business)
        response_object = {
            'status': 'success',
            'message': 'Business created successfully',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'This business already exists.',
        }
        return response_object, 409


def get_all_business():
    return Business.query.all()


def get_business(business_name):
    return Business.query.filter_by(business_name=business_name).first()


def delete_business(business_name):
    db.session.delete(business_name)
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
