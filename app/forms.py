from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from .models import Genre

class BookForm(FlaskForm):
    title = StringField('Название книги', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    genre = SelectField('Жанр', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Добавить книгу')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.genre.choices = [(genre.id, genre.name) for genre in Genre.query.order_by(Genre.name).all()]

