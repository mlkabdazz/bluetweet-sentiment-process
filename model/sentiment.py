from run import db


class Sentiment(db.Model):
    """Model table sentiment"""

    id = db.Column(db.String, primary_key=True)
    word = db.Column(db.String)
    value = db.Column(db.String)
    create_at = db.Column(db.DateTime)

    def __init__(self, id, word, value, create_at):
        self.id = id
        self.word = word
        self.value = value
        self.create_at = create_at
