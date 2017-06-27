from flask_server import db
from datetime import datetime

class Formula(db.Model):
    __tablename__ = 'formula'
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(80), nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.String(250))

    instructions = db.Column(db.String(1000))

    user_key = db.Column(db.String(80))

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def get_password(self):
        return self.password