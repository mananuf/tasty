from eatapp import app, db


# ------------------------- USERS MODEL -----------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)   # user id
    username = db.Column(db.String(25), unique=True, nullable=False)    # username field
    email = db.Column(db.String(120), unique=True, nullable=False)      # email field
    password = db.Column(db.String(60), unique=False, nullable=False)   # password field
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')    # image field