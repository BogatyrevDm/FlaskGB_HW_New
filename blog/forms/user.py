from wtforms import Form, StringField, validators, PasswordField, SubmitField


class UserRegisterForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm password', [validators.DataRequired()])
    submit = SubmitField('Register')