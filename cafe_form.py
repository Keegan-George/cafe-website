from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, URL


class CafeForm(FlaskForm):
    name = StringField(label="Name:", validators=[InputRequired()])
    location = StringField(label="Location:", validators=[InputRequired()])
    map_url = StringField(label="Google Map URL:", validators=[InputRequired(), URL()])
    img_url = StringField(label="Image URL:", validators=[URL()])
    has_sockets = BooleanField(label="Has Sockets:")
    has_toilet = BooleanField(label="Has Toilets:")
    has_wifi = BooleanField(label="Has Wifi:")
    can_take_calls = BooleanField(label="Can Take Calls:")
    seats = StringField(label="Number of Seats:", validators=[InputRequired()])
    coffee_price = StringField(label="Coffee Price:", validators=[InputRequired()])
    submit = SubmitField(label="Submit")
