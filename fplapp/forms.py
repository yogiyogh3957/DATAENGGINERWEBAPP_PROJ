from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from fplapp import db
from fplapp.models import FPLplayers

def team_dropdown(choice):
    all_team = db.session.query(FPLplayers.team)
    teamlist = [" "]
    for t in all_team:
        a = str(t).split("('")[1].split("',)")[0]
        if a in teamlist:
            pass
        else:
            teamlist.append(a)
    if choice == 1 :
        return teamlist

class QueryForm(FlaskForm):
    team  = SelectField('Team', validators=[DataRequired()], choices=team_dropdown(1))
    players = SelectField('Players', validators=[DataRequired()], choices=[])

    team2 = SelectField('Team2', validators=[DataRequired()], choices=team_dropdown(1))
    players2 = SelectField('Players2', validators=[DataRequired()], choices=[])

    submit  = SubmitField('Compare Now!')