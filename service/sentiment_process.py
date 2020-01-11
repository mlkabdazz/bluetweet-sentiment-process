from model import AccountTweet

import tweepy
from textblob import TextBlob
import json
import nltk
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer


# from pyspark import SparkContex

def on_status(self):
    """Process to extract sentiment"""
    results = AccountTweet.query.all()
    for result in results:
        tweet = result.tweet
        tweet_clean = text_cleaner(tweet)
        sentiment = my_grandpa_trnsltr(tweet_clean)
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity

        print('<><><><>', polarity)
        print('++++++++', subjectivity)
        return 'OKE'


def text_cleaner(self, text):
    """Cleaning text before translate"""
    text = text.lower()
    factory_cleaning = StopWordRemoverFactory().create_stop_word_remover()
    text = factory_cleaning.remove(text)
    factory_stemmer = StemmerFactory().create_stemmer()
    return factory_stemmer.stem(text)


def my_grandpa_trnsltr(self, text_cleaner):
    """My grandpa is the best translator wkwkwkwk. jk bro :p"""
    return TextBlob(text_cleaner).translate('id', 'en')
