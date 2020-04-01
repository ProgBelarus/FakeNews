from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, FieldList, FormField
from wtforms.validators import Length


class EvaluateArticleForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('real', 'Legitimate'), ('fake', 'Fake'), ('satire', 'Satire'),
        ('partisan', 'Extreme Partisan Bias'), ('conspiracy', 'Conspiracy Theory'),
        ('opinion', 'Opinion'), ('convoluted', 'Convoluted')])
    comment = TextAreaField('Comment', validators=[Length(max=1000)])


class EvaluateManyArticlesForm(FlaskForm):
    evals = FieldList(FormField(EvaluateArticleForm), min_entries=20)
    submit = SubmitField('Submit')
