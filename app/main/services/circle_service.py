import uuid, datetime
from app.main import db
from app.main.models.circle import Circle
from app.main.services.help import Helper

def save_new_circle(data):
    new_circle = Circle(
        public_id = str(uuid.uuid4()),
        circle_name = data["circleName"]
    )

    Helper.save_changes(new_circle)

    return Helper.generate_token("Circle", new_circle)

def get_all_circles():
    return Circle.query.all()

def get_a_circle(public_id):
    return Circle.query.filter_by(public_id=public_id).first()

def delete_circle(public_id):
    circle = Circle.query.filter_by(public_id=public_id).first()

    if circle:
        db.session.delete(circle)

        db.session.commit()

        return Helper.return_resp_obj("success", "Circle deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No circle found.", None, 409)

def update_circle(public_id, data):
    circle = Circle.query.filter_by(public_id=public_id).first()
    
    circle.circle_name = data["circleName"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Circle updated successfully.", None, 200)