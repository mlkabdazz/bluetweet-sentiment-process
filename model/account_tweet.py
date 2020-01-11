from run import db

class AccountTweet(db.Model):
    """model table account tweet"""

    id = db.Column(db.String, primary_key=True)
    account_id = db.Column(db.String)
    twitter_id = db.Column(db.Integer)
    tweet = db.Column(db.String)
    tweet_created_at = db.Column(db.DateTime)
    create_at = db.Column(db.DateTime)

    def __init(self, id, account_id, twitter_id, tweet, tweet_created_at, create_at):
        self.id = id
        self.account_id = account_id
        self.twitter_id = twitter_id
        self.tweet = tweet
        self.tweet_created_at = tweet_created_at
        self.create_at = create_at
