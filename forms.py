from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
    SelectField
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp,optional
from wtforms.fields.html5 import DateField
import email_validator
import flask_login
from flask_login import current_user
from wtforms import ValidationError
from wtforms import validators


class MakeAppointment(FlaskForm):
    phone_no = StringField(validators=[InputRequired(), Length(10,10)])
    date = DateField('DatePicker', format='%Y-%m-%d')
    doctor = SelectField(choices=[('Select'),('Cardiologist'),('Allergist'),('Dentist'),('Paditrician'),('Dermatologist'),('Not sure-Leave a message')])
    message = TextAreaField(validators=[optional()])






