import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(first_name='user', last_name='userov', email='name@example.com',
                 password=generate_password_hash('test123'))
        )
        db.session.commit()


@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    tags = ('flask', 'django', 'python', 'geekbrains', 'sqllite')

    with app.app_context():
        for item in tags:
            tag = Tag(name=item)
            db.session.add(tag)
        db.session.commit()
    click.echo(f'Created tags {", ".join(tags)}')


@click.command('create-init-author')
def create_init_author():
    from blog.models import Author
    from wsgi import app

    with app.app_context():
        db.session.add(
            Author(user_id=1)
        )
        db.session.commit()
