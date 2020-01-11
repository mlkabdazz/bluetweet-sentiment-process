from apps.run import db
from apps.config import Base


class Sentiment(Base):
    """sentiment model or entity"""

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String())
    value = db.Column(db.String())
    create_at = db.Column(db.Date)

    def __init__(self, id, word, value, create_at):
        self.id = id
        self.word = word
        self.value = value
        self.create_at = create_at