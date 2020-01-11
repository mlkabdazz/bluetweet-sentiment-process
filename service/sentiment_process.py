from model import AccountTweet, Sentiment

from textblob import TextBlob
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def on_status():
    """Process to extract sentiment"""
    results = AccountTweet.query.all()
    sentiment_negative = 0.0
    sentiment_normal = 0.0
    sentiment_positive = 0.0

    for result in results:
        tweet = result.tweet
        tweet_clean = text_cleaner(tweet)
        sentiment = my_grandpa_trnsltr(tweet_clean)
        # print(type(sentiment))
        polarity = sentiment
        # subjectivity = sentiment.subjectivity/

        print("Running sentiment process...")

        if (polarity is not 'x'):
            if (polarity < 0):
                # print('Negative : ', polarity)
                sentiment_negative += 1

            if (polarity > 0):
                # print('Positive : ', polarity)
                sentiment_positive += 1

            if (polarity == 0):
                # print('Normal : ', polarity)
                sentiment_normal += 1

        # print('Positive : ', sentiment_positive)
        # print('Negative : ', sentiment_negative)
        # print('Normal : ',sentiment_normal)
        # print('++++++++', subjectivity)
    print('Positive : ', sentiment_positive)
    print('Negative : ', sentiment_negative)
    print('Normal : ', sentiment_normal)
    result_sentiment = [sentiment_positive, sentiment_normal, sentiment_negative]
    return result_sentiment


def text_cleaner(text):
    """Cleaning text before translate"""
    text = text.lower()
    factory_cleaning = StopWordRemoverFactory().create_stop_word_remover()
    text = factory_cleaning.remove(text)
    factory_stemmer = StemmerFactory().create_stemmer()
    return factory_stemmer.stem(text)


def my_grandpa_trnsltr(text_cleaner):
    """My grandpa is the best translator wkwkwkwk. jk bro :p"""
    try:
        pol = TextBlob(text_cleaner).translate(from_lang='id', to='en')
        return pol.polarity
    except:
        print('Same translation, skip ae bos !')
        return 'x'