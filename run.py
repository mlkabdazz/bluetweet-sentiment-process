from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller import sentiment_blueprint, account_tweet_ctrl


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uuuvydfagounha:0a09d4304d05a75ae81ed01b353d9a2c44e13c41c41a3e0c860b398a80ba25e9@ec2-174-129-255-76.compute-1.amazonaws.com:5432/d6binvd45dcfp8'
# app.config['SECRET_KEY'] = '0a09d4304d05a75ae81ed01b353d9a2c44e13c41c41a3e0c860b398a80ba25e9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/bluetweets_dev'
app.config['SECRET_KEY'] = 'postgres'

db = SQLAlchemy(app)

app.register_blueprint(sentiment_blueprint)
app.register_blueprint(account_tweet_ctrl)


@app.route("/")
def home():
    return "this your home"


if __name__ == '__main__':
    app.run(debug=True)
