from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
import wtforms.validators
from flask_ckeditor import CKEditorField
from wtforms import validators

class LoginForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    submit = SubmitField("Sign In")

class RegisterForm(FlaskForm):
    email = StringField(label='Email address', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    name = StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = SubmitField("Sign Up!")

class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[wtforms.validators.DataRequired()])
    map_url = StringField("Map URL", validators=[wtforms.validators.DataRequired(), wtforms.validators.URL()])
    img_url = StringField("Image URL", validators=[wtforms.validators.DataRequired(), wtforms.validators.URL()])
    location = StringField("Location", validators=[wtforms.validators.DataRequired()])
    seats = StringField("Number Of Seats")
    has_toilet = SelectField("Restrooms", choices=[("", "---"), (1,'Yes'), (0, 'No')])
    has_wifi = SelectField("Wi-Fi", choices=[("", "---"), (1, 'Yes'), (0, 'No')])
    has_sockets = SelectField("Outlets", choices=[("", "---"), (1, 'Yes'), (0, 'No')])
    can_take_calls = SelectField("Can Take Calls", choices=[("", "---"), (1, 'Yes'), (0, 'No')])
    coffee_price = StringField("Price Of Coffee")
    submit = SubmitField("Add Cafe")
