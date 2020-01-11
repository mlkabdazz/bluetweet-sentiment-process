from flask import Blueprint

account_tweet_ctrl = Blueprint('account_tweet_ctrl', __name__)


@account_tweet_ctrl.route("/accounttweetprocess")
def tweetprocess():
    from service import sentiment_process
    # sentiment_process()
    return "your sentiment calculation success"
