from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace("auth", description="authentication related operations")

    user_auth = api.model("user_auth", {
        "username_or_email" : fields.String(required=True, description="user username or email address"),
        "password" : fields.String(required=True, description="user password")
    })

    parser = api.parser()

    # parser.add_argument("username_or_email", type=str, help="user username or email address", location="form")
    # parser.add_argument("password", type=str, help="user password", location="form")

class UserDto:
    api = Namespace("user", description="user related operations")

    user = api.model("user", {
        "first_name" : fields.String(required=True, description="user first name"),
        "last_name" : fields.String(required=True, description="user last name"),
        "bio" : fields.String(required=True, description="user bio"),
        "email" : fields.String(required=True, description="user email"),
        "username" : fields.String(required=True, description="user username"),
        "contact_no" : fields.String(required=False, description="user contact number")
    })

    parser = api.parser()

class PetDto:
    api = Namespace("pet", description="pet related operations")

    pet = api.model("pet", {
        "public_id" : fields.String(required=True, description="pet public id"),
        "pet_name" : fields.String(required=True, description="pet name"),
        "bio" : fields.String(required=True, description="pet bio"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=False, description="pet birthday"),
        "sex" : fields.String(required=True, description="pet sex"),
        "profPic_filename" : fields.String(required=True, description="pet large profile picture"),
        "specie_name" : fields.String(required=True, description="pet specie"),
        "breed_name" : fields.String(required=True, description="pet breed"),
    })

    parser = api.parser()

class SpecieDto:
    api = Namespace("specie", description="specie related operations")

    specie = api.model("specie", {
        "public_id" : fields.String(required=True, description="specie public id"),
        "specie_name" : fields.String(required=True, description="specie name")
    })

    parser = api.parser()

class BreedDto:
    api = Namespace("breed", description="breed related operations")

    breed = api.model("breed", {
        "breed_name": fields.String(required=True, description="breed name"),
        "public_id" : fields.String(require=True, description="breed public id")
    })

    parser = api.parser()

class CircleDto:
    api = Namespace("circle", description="circle related operations")

    circle = api.model("circle", {
        "circle_name" : fields.String(required=True, description="circle name")
    })

    parser = api.parser()

class BusinessDto:
    api = Namespace("business", description="business related operations")

    business = api.model("business", {
        "business_name" : fields.String(required=True, description="business email address"),
        "address": fields.String(required=False, description="business address"),
        "contact_no" : fields.String(required=False, description="business contact number")
    })

    parser = api.parser()
