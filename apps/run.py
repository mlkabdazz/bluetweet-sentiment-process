from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apps.src.views import account_tweet_blueprint, home_blueprint
from datetime import datetime
from apps.src.models.account_tweet import AccountTweet


app = Flask(__name__)
app.config['DEBUG'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://uuuvydfagounha:0a09d4304d05a75ae81ed01b353d9a2c44e13c41c41a3e0c860b398a80ba25e9@ec2-174-129-255-76.compute-1.amazonaws.com:5432/d6binvd45dcfp8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(home_blueprint)
app.register_blueprint(account_tweet_blueprint)


# class AccountTweet(db.Model):
#     id = db.Column(db.String(), primary_key=True)
#     account_id = db.Column(db.String)
#     twitter_id = db.Column(db.Integer)
#     tweet = db.Column(db.String())
#     tweet_created_at = db.Column(db.DateTime)
#     create_at = db.Column(db.DateTime)
#
#     def __init__(self, idinternal, account_id, twitter_id, tweet, tweet_created_at, create_at):
#         self.id = idinternal
#         self.account_id = account_id
#         self.twitter_id = twitter_id
#         self.tweet = tweet
#         self.tweet_created_at = tweet_created_at
#         self.create_at = create_at


@app.route("/wkwk")
def wkwk():
    accountTweet = AccountTweet('ad16ac17-056f-4197-afba-4f1fc6a009fa', 'cebabed5-f055-4050-9a4d-3f9547de25aa', 1209771710251032578, '@AndiArief__ Selamat buat wak @jokowi', datetime.now(), datetime.now())
    return accountTweet.create_at


# @app.route("/test")
# def test():
#     text_lower = "makan nasi"
#     factory = StopWordRemoverFactory()
#     stopword = factory.create_stop_word_remover()
#     stop = stopword.remove(text_lower)
#     factory = StemmerFactory()
#     stemmer = factory.create_stemmer()
#     katadasar = stemmer.stem(stop)
#
#     text_en=TextBlob(katadasar).translate(from_lang='id',to='en')
#     sentiment = text_en.sentiment
#     polarity = sentiment.polarity
#     subjectivity = sentiment.subjectivity
#
#     return str(text_en.sentiment)

app.run(debug=True)
