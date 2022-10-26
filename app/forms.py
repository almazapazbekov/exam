from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, DateField, validators, ValidationError

from .models import Position


class PositionForm(FlaskForm):
    name = StringField(label='Название должности', validators=[validators.DataRequired()])
    department = StringField(label='Название отдела')
    wage = IntegerField(label='Заработная плата', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить должность')


class EmployeeForm(FlaskForm):
    name = StringField(label='ФИО сотрудника', validators=[validators.DataRequired()])
    birth_date = DateField(label='Дата рождения', validators=[validators.DataRequired()])
    position_id = SelectField(label='Выбор должности', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить сотрудника')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for position in Position.query.all():
            result.append((position.id ,position.name))
        self.position_id.choices = result

    def validate_wage(self, wage):
        if wage.data < 0:
            raise ValidationError('ЗП не может быть меньше нуля (но можно 0, т.е стажер)')
