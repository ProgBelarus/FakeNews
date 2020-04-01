from app.eval import eval1
from app import db
from app.eval.models import Evaluation
from app.catalog.models import Publication, Book
from flask_security import current_user
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.eval.forms import EvaluateManyArticlesForm
import numpy as np

@eval1.route('/evaluation', methods=['GET', 'POST'])
def display_eval_form():
    form = EvaluateManyArticlesForm(request.form)
    articles = np.random.choice(Book.query.all(), size=20, replace=False)
    if form.validate_on_submit():
        cnt=0
        form_id = np.random.randint(10000000)
        for entry in form.evals.entries:
            Evaluation.create_evaluation(form_id=form_id, category=entry.data['category'], comments=entry.data['comment'], article_id=articles[cnt].id, user_id=current_user.id)
            cnt += 1
        return render_template('evaluation_results.html', form_id=form_id)
    return render_template('evaluation_prompt.html', EvalForm=form, Articles=articles, zip=zip)

# @main.route('/display/publisher/<publisher_id>')
# def display_publisher(publisher_id):
#     publisher = Publication.query.filter_by(id=publisher_id).first()
#     publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
#     return render_template('publisher.html',
#                            publisher=publisher,
#                            publisher_books=publisher_books)
#
#
# @main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
# @login_required
# def delete_book(book_id):
#     book = Book.query.get(book_id)
#     if request.method == 'POST':
#         db.session.delete(book)
#         db.session.commit()
#         flash('book delete successfully')
#         return redirect(url_for('main.display_books'))
#     return render_template('delete_book.html', book=book, book_id=book.id)
#
#
# @main.route('/evaluation', methods=['GET', 'POST'])
# @login_required
# def eval_books():
#     book = Book.query.get(book_id)
#     form = EditBookForm(obj=book)
#     if form.validate_on_submit():
#         book.title = form.title.data
#         book.format = form.format.data
#         book.num_pages = form.num_pages.data
#         db.session.add(book)
#         db.session.commit()
#         flash('Book Edited Successfully')
#         return redirect(url_for('main.display_books'))
#     return render_template('edit_book.html', form=form)
#
#
# @main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
# @login_required
# def create_book(pub_id):
#     form = CreateBookForm()
#     form.pub_id.data = pub_id  # pre-populates pub_id
#     if form.validate_on_submit():
#         book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data,
#                     book_format=form.format.data, image=form.img_url.data, num_pages=form.num_pages.data,
#                     pub_id=form.pub_id.data)
#         db.session.add(book)
#         db.session.commit()
#         flash('Book added successfully')
#         return redirect(url_for('main.display_publisher', publisher_id=pub_id))
#     return render_template('create_book.html', form=form, pub_id=pub_id)