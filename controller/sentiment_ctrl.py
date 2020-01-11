from flask import Blueprint
from datetime import datetime

sentiment_blueprint = Blueprint('sentiment_blueprint', __name__)


@sentiment_blueprint.route("/sentiment/process")
def sentiment_controller():
    from service import on_status
    from model import Sentiment as sentiment
    from run import db
    result_sentiment = on_status()
    sentiment_positve = result_sentiment[0]
    sentiment_negative = result_sentiment[1]
    sentiment_normal = result_sentiment[2]

    total_hasil_sentiment = sentiment_positve + sentiment_negative + sentiment_normal

    sentiment_positve = ((sentiment_positve / total_hasil_sentiment) * 100)
    sentiment_normal = ((sentiment_normal / total_hasil_sentiment) * 100)
    sentiment_negative = ((sentiment_negative / total_hasil_sentiment) * 100)

    print("persentase positive : ", sentiment_positve)
    print("persentase negative : ", sentiment_negative)
    print("persentase normal : ", sentiment_normal)

    sentiment_pos = sentiment('1', 'POSITIF', sentiment_positve, datetime.now())
    sentiment_neg = sentiment('2', 'NEGATIF', sentiment_negative, datetime.now())
    sentiment_nor = sentiment('3', 'NORMAL', sentiment_normal, datetime.now())
    db.session.add(sentiment_pos)
    db.session.add(sentiment_neg)
    db.session.add(sentiment_nor)
    db.session.commit()

    return "process sentiment success"


    # from model import Sentiment
    # result = Sentiment.query.all()
    # for rs in result:
    #     print(rs.word, " : ",rs.value)