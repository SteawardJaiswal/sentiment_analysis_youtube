from textblob import TextBlob

def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        sentiments.append(analysis.sentiment.polarity)
    return sentiments
