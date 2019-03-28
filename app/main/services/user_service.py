import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_name=str(uuid.uuid4()),
            email=data['email'],  # contacts, admins, members
            contact=data['contact'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_name):
    return User.query.filter_by(public_name=public_name).first()


def delete_user(public_name):
    user = User.query.filter_by(public_name=public_name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'user has been deleted'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'failed',
            'message': 'No user found'
        }
        return response_object, 409


def update_user(public_name):
    user = User.query.filterby(public_name=public_name).first()
    if user:
        user.public_name = str(uuid.uuid4()),
        user.email = ['email'],
        user.contact = ['contact'],
        user.username = ['username'],
        user.password = ['password'],
        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'User updated!'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'Failed',
            'message': 'No user found'
        }
        return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
