from flask import Blueprint

sentiment_blueprint = Blueprint('sentiment_blueprint', __name__)


@sentiment_blueprint.route("/sentiment")
def sentiment_controller():
    from model import Sentiment
    result = Sentiment.query.all()
    for rs in result:
        print(rs.word)
    return "oke"