from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, validators


class CreateArticleForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    tags = SelectMultipleField(
        "Tags", coerce=int
    )
    submit = SubmitField("Publish")