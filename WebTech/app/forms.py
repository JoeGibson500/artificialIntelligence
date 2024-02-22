from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# range may be changed to allow more users, code adapts to this automatically
class LoginForm(FlaskForm):
    id = SelectField('Number', choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
        ], validators=[DataRequired()])


class IncExpForm(FlaskForm):
    amount = DecimalField('amount', places=2, rounding=None,
                          validators=[DataRequired()])
    desc = TextAreaField('desc', validators=[DataRequired()])


class SetGoalForm(FlaskForm):
    number1 = DecimalField('number1', places=2, rounding=None,
                           validators=[DataRequired()])


class DelGoalForm(FlaskForm):
    submit_button = SubmitField('Enter')
