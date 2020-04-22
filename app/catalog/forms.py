from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField
from wtforms.validators import DataRequired


# class EditBookForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     format = StringField('Format', validators=[DataRequired()])
#     num_pages = StringField('Pages', validators=[DataRequired()])
#     submit = SubmitField('Update')
#
#

# class CreateArticleForm(FlaskForm):
#
#     title = StringField('Title', validators=[DataRequired()])
#     subtitle = StringField('Subtitle', validators=[DataRequired()])
#     text = StringField('Text', validators=[DataRequired()])
#     url = StringField('URL', validators=[DataRequired()])
#     publication = StringField('Source', validators=[DataRequired()])
#     pub_date = DateField('Publication Date', validators=[DataRequired()])
#     is_gold = BooleanField('Gold Standard?', validators=[DataRequired()])
#     submit = SubmitField('Create')