from app.eval import eval1
from app import db
from app.eval.models import Evaluation
from app.catalog.models import Publication, Article
from flask_security import current_user
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.eval.forms import EvaluateArticleForm, EvaluateManyArticlesForm
import numpy as np
import random

@eval1.route('/evaluation', methods=['GET', 'POST'])
@login_required
def display_eval_form():
    form = EvaluateManyArticlesForm(request.form)

    if form.validate_on_submit():
        form_id = np.random.randint(10000000)
        for entry in form.evals.entries:
            Evaluation.create_evaluation(form_id=form_id,
                                         category=entry.data['category'],
                                         comments=entry.data['comment'],
                                         article_id=int(entry.data['article_id']),
                                         user_id=current_user.id)
        return render_template('evaluation_results.html', form_id=form_id)

    test_articles = Article.query.filter_by(is_gold=False).all()
    gold_articles = Article.query.filter_by(is_gold=True).all()
    articles = list(np.random.choice(test_articles, size=10, replace=False))
    articles.extend(gold_articles[:10])
    random.shuffle(articles)

    cnt = 0
    for article_form in form.evals.entries:
        article_form.article_id.data = str(articles[cnt].id)
        cnt += 1

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