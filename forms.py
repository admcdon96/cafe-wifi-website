from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import wtforms.validators
from flask_ckeditor import CKEditorField
from wtforms import validators

class LoginForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    submit = SubmitField("SIGN IN")

class RegisterForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    name = StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = SubmitField("SIGN ME UP!")