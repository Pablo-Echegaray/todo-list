from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return f'<User: {self.username}>'