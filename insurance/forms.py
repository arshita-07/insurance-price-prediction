from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,  FloatField, SelectField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    age = IntegerField(label = 'Age', validators=[DataRequired()])
    gender = SelectField(label= 'Gender', choices=[('female','female'),('male','male')])
    bmi = FloatField(label="BMI", validators=[DataRequired()])
    no_children = IntegerField(label = 'Number of children')
    smoker = SelectField(label= 'Do you smoke?', choices=[('yes','yes'),('no','no')])
    region = SelectField(label= 'Region', choices=[('northeast','northeast'),('northwest','northwest'),('southeast','southeast'),('southwest','southwest')])
    submit = SubmitField('Submit')