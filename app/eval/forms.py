from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, FieldList, FormField, HiddenField
from wtforms.validators import Length


class EvaluateArticleForm(FlaskForm):
    article_id = HiddenField()
    category = SelectField('Category', choices=[
        ('real', 'Legitimate'), ('fake', 'Fake'), ('satire', 'Satire'),
        ('bias', 'Biased Reporting'), ('conspiracy', 'Conspiratorial Thinking'),
        ('opinion', 'Opinion'), ('bad', 'Not a Valid Article (please explain why in the Comment box)')])
    comment = TextAreaField('Comment', validators=[Length(max=1000)])


class EvaluateManyArticlesForm(FlaskForm):
    evals = FieldList(FormField(EvaluateArticleForm), min_entries=20)
    submit = SubmitField('Submit')
