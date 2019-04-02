from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок объявления', validators=[DataRequired()])
    content = TextAreaField('Текст объявления', validators=[DataRequired()])
    submit = SubmitField('Добавить')