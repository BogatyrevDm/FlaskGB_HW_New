from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.forms.user import UserRegisterForm
from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)

    return render_template(
        'users/register.html',
        form=form
    )


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"User #{pk} doesn't exist!")

    return render_template(
        'users/profile.html',
        user=selected_user,
    )
