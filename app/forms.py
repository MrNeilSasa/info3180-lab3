from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask import Markup

class ContactForm(FlaskForm):
    name = StringField(Markup('Name <span style="color:red;">(Required)</span>'), validators=[InputRequired()])
    email = StringField(Markup('Email <span style="color:red;">(Required)</span>'), validators=[InputRequired(), Email()])
    subject = StringField(Markup('Subject <span style="color:red;">(Required)</span>'), validators=[InputRequired()])
    message = TextAreaField(Markup('Message <span style="color:red;">(Required)</span>'), validators=[InputRequired()])

