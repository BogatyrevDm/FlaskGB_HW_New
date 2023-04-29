import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
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
