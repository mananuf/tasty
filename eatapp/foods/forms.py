from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, DecimalField
from wtforms.validators import DataRequired


# ------------------------------ ADD FOOD ---------------------------
class AddFood(FlaskForm):
    food_name = StringField('Food Name', validators=[DataRequired()])   # name field
    price = DecimalField('Price', validators=[DataRequired()])          # price field
    discount = IntegerField('Discount', default=0)                      # discount field
    stock = IntegerField('Stock', validators=[DataRequired()])          # Stock field
    description = TextAreaField('Description', validators=[DataRequired()])     # description

    image = FileField('image', validators=[FileAllowed(['jpg','jpeg','png','gif'], 'images only!')])     # image field