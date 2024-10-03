from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import Book, Genre
from .forms import BookForm
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)

@bp.route('/genre/<int:genre_id>')
def genre_page(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books = genre.books.order_by(Book.created_at.desc()).all()
    return render_template('genre.html', genre=genre, books=books)

@bp.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, genre_id=form.genre.data)
        db.session.add(book)
        db.session.commit()
        flash('Книга добавлена успешно!')
        return redirect(url_for('main.index'))
    return render_template('add_book.html', form=form)
