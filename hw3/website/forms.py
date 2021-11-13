from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField

from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    cityname = StringField('City Name', validators=[DataRequired()])
    cityrank = IntegerField('City Rank', validators=[DataRequired()])
    visited = BooleanField('Visited')

    submit = SubmitField('Submit')

