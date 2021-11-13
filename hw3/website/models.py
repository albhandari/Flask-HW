from website import db
from flask_login import UserMixin

class City(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cityname = db.Column(db.String(64))
    cityrank = db.Column(db.Integer)
    visited = db.Column(db.Boolean)

    def __repr__(self):
        return f'{self.cityname}'

    
 




