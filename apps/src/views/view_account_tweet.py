from flask import Blueprint

account_tweet_blueprint = Blueprint('accounttweet', __name__)


@account_tweet_blueprint.route("/accounttweet")
def account_tweets():

    return 'hello malik, lagi lagi malik'
