from datetime import datetime
from email.mime import image
from eatapp import db, app



# ------------------------- FOOD MODEL -----------------------

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(80), nullable=False)    # name field
    price= db.Column(db.Numeric(10,2), nullable=False)      # price field
    discount = db.Column(db.Integer, default=0)             # discount
    stock = db.Column(db.Integer, nullable=False)           # stock
    description = db.Column(db.Text, nullable=False)        # description
    date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)                            # date

    # relationship
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
        nullable=False)
    category = db.relationship('Categories',
        backref=db.backref('categories', lazy=True))

    image = db.Column(db.String(150), nullable=False, default="image.png")

    def __repr__(self):
        return '<Food %r>' % self.food_name


# ------------------------- CATEGORY MODEL -----------------------
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)   # user id
    category_name = db.Column(db.String(50), unique=True, nullable=False)    # username field


