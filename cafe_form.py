from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, URL


class CafeForm(FlaskForm):
    name = StringField(label="Name:", validators=[InputRequired()])
    map_url = StringField(label="Google map url:", validators=[InputRequired(), URL()])
    img_url = StringField(label="Image url:", validators=[URL()])
    location = StringField(label="Location:", validators=[InputRequired()])
    has_sockets = BooleanField(label="Has sockets:")
    has_toilet = BooleanField(label="Has toilets:")
    has_wifi = BooleanField(label="Has wifi:")
    can_take_calls = BooleanField(label="Can take calls:")
    seats = StringField(label="Number of seats:", validators=[InputRequired()])
    coffee_price = StringField(label="Coffee price:", validators=[InputRequired()])
    submit = SubmitField(label="Submit")
