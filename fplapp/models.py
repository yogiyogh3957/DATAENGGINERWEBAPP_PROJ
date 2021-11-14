from fplapp import db

class FPLplayers(db.Model):
    __tablename__ = 'players_table_withcode'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    team = db.Column(db.Text)
    position = db.Column(db.Text)
    goals_score = db.Column(db.Integer)
    goals_conceded = db.Column(db.Integer)
    total_points = db.Column(db.Integer)
    price = db.Column(db.Integer)
    code = db.Column(db.Integer)