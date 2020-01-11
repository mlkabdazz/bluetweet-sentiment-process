from run import db


class Dev01(db.Model):
    idn = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, idn, name):
        self.idn = idn
        self.name = name

