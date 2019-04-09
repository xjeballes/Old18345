from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'contact': fields.String(required=False, description='user contact'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_name': fields.String(description='user Identifier')
    })

    parser = api.parser()
    parser.add_argument('email', type=str, help='user email address', location='form')
    parser.add_argument('contact', type=str, help='user contact number', location='form')
    parser.add_argument('username', type=str, help='user username', location='form')
    parser.add_argument('password', type=str, help='user password', location='form')
    parser.add_argument('public_name', type=str, help='user identifier', location='form')


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

    parser = api.parser()
    parser.add_argument('email', type=str, help='user email address', location='form')
    parser.add_argument('password', type=str, help='user password', location='form')


class CircleDto:
    api = Namespace('circle', description='circle related operations')
    circle = api.model('circle', {
        'email': fields.String(required=True, description='circle email address'),
        'contact_num': fields.String(description='circle contact'),
        'circle_name': fields.String(description='circle Identifier')
    })


class BusinessDto:
    api = Namespace('business', description='business related operations')
    business = api.model('business', {
        'email': fields.String(required=True, description='business email address'),
        'contact_num': fields.String(description='business contact number'),
        'address': fields.String(description='business address'),
        'business_name': fields.String(description='business Identifier')
    })
