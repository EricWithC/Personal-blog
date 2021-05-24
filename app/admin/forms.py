from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Tag

def tag(name):
    return Tag.query.filter_by(name=name).first()

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=0, max=140)])
    body = TextAreaField('Body', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', coerce=tag)
    submit = SubmitField('Submit')

class TagForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=0, max=50)])
    submit = SubmitField('Submit')