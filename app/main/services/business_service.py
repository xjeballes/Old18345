import uuid, datetime
from app.main import db
from app.main.models.business import Business
from app.main.services.help import Helper

def save_new_business(data):
    new_business = Business(
        public_id = str(uuid.uuid4()),
        business_name = data["businessName"],
        address = data["address"],
        contact_no = data["contactNo"]
    )

    Helper.save_changes(new_business)

    return Helper.generate_token(new_business)

def get_all_businesses():
    return Business.query.all()

def get_a_business(public_id):
    return Business.query.filter_by(public_id=public_id).first()

def delete_business(public_id):
    business = Business.query.filter_by(public_id=public_id).first()

    if business:
        db.session.delete(business)

        db.session.commit()

        return Helper.return_resp_obj("success", "Business deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No business found.", None, 409)

def update_business(public_id, data):
    business = Business.query.filter_by(public_id=public_id).first()
    
    business.business_name = data["businessName"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Business updated successfully.", None, 200)

def save_changes(data):
    db.session.add(data)

    db.session.commit()

def generate_token(business):
    try:
        auth_token = Helper.encode_auth_token(business.public_id)

        return Helper.return_resp_obj("success", "Business registered successfully.", auth_token, 201)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Some error occured.", None, 401)