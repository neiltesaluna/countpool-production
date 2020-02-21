from countpool import db

class Timer (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    goal = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default-1.jpg')

    def __repr__(self):
        return f"Timer('{self.title}','{self.goal}')"
