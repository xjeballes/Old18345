from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace("user", description="user related operations")

    user = api.model("user", {
        "first_name" : fields.String(required=True, description="user first name"),
        "last_name" : fields.String(required=True, description="user last name"),
        "email" : fields.String(required=True, description="user email address"),
        "username" : fields.String(required=True, description="user username"),
        "contact_no" : fields.String(required=False, description="user contact no")
    })

    parser = api.parser()

    parser.add_argument("first_name", type=str, help="user first name", location="form")
    parser.add_argument("last_name", type=str, help="user first name", location="form")
    parser.add_argument("email", type=str, help="user email address", location="form")
    parser.add_argument("username", type=str, help="user username", location="form")
    parser.add_argument("contact_no", type=str, help="user contact number", location="form")
    parser.add_argument("password", type=str, help="user password", location="form")
    parser.add_argument("confirm_password", type=str, help="user confirm password", location="form")

class AuthDto:
    api = Namespace("auth", description="authentication related operations")

    user_auth = api.model("user_auth", {
        "username_or_email" : fields.String(required=True, description="user username or email address"),
        "password" : fields.String(required=True, description="user password")
    })

    parser = api.parser()

    parser.add_argument("username_or_email", type=str, help="user username or email address", location="form")
    parser.add_argument("password", type=str, help="user password", location="form")

class PetDto:
    api = Namespace("pet", description="pet related operations")

    pet = api.model("pet", {
        "pet_name" : fields.String(required=True, description="pet name"),
        "public_id" : fields.String(required=True, description="pet public id"),
        "sex" : fields.String(required=True, description="pet sex"),
        "specie_name" : fields.String(required=True, description="pet specie"),
        "breed_name" : fields.String(required=True, description="pet breed"),
        "profPic_filename" : fields.String(required=True, description="pet large profile picture"),
        "profPic_sm_filename" : fields.String(required=True, description="pet small profile picture")
    })

    parser = api.parser()

    parser.add_argument("pet_name", type=str, help="pet name", location="form")
    parser.add_argument("public_id", type=str, help="pet public id", location="form")
    parser.add_argument("sex", type=str, help="pet sex", location="form")
    parser.add_argument("specie_name", type=str, help="pet specie", location="form")
    parser.add_argument("breed_name", type=str, help="pet breed", location="form")

class SpecieDto:
    api = Namespace("specie", description="specie related operations")

    specie = api.model("specie", {
        "public_id" : fields.String(required=True, description="specie public id"),
        "specie_name" : fields.String(required=True, description="specie name")
    })

    parser = api.parser()

    parser.add_argument("public_id", type=str, help="specie public id", location="form")
    parser.add_argument("specie_name", type=str, help="specie name", location="form")

class BreedDto:
    api = Namespace("breed", description="breed related operations")

    breed = api.model("breed", {
        "breed_name": fields.String(required=True, description="breed name"),
        "public_id" : fields.String(require=True, description="breed public id")
    })

    parser = api.parser()

    parser.add_argument("breed_name", type=str, help="breed name", location="form")
    parser.add_argument("public_id", type=str, help="breed public id", location="form")

class CircleDto:
    api = Namespace("circle", description="circle related operations")

    circle = api.model("circle", {
        "circle_name" : fields.String(required=True, description="circle name")
    })

    parser = api.parser()

    parser.add_argument("circle_name", type=str, help="circle name", location="form")

class BusinessDto:
    api = Namespace("business", description="business related operations")

    business = api.model("business", {
        "business_name" : fields.String(required=True, description="business email address"),
        "address": fields.String(required=False, description="business address"),
        "contact_no" : fields.String(required=False, description="business contact number")
    })

    parser = api.parser()

    parser.add_argument("business_name", type=str, help="business name", location="form")
    parser.add_argument("address", type=str, help="business address", location="form")
    parser.add_argument("contact_no", type=str, help="business contact number", location="form")
    
