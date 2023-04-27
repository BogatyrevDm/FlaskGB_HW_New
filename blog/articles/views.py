from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


@article.route('/<int:article_id>', methods=['GET'])
def article_detail(article_id):
    _article: Article = Article.query.filter_by(id=article_id).one_or_none()
    if not _article:
        raise NotFound
    return render_template(
        'articles/details.html',
        article=_article,
    )


@article.route('/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template('articles/create.html', form=form)


@article.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        db.session.add(_article)
        if current_user.author:
            _article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            _article.author = current_user.author

        db.session.commit()

        return redirect(url_for('article.details', article_id=_article.id))

    return render_template('articles/create.html', form=form)
