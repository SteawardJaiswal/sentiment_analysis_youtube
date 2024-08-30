from flask import Blueprint, render_template, request
from .youtube_api import fetch_comments
from .sentiment_analysis import analyze_sentiment

blueprint = Blueprint('main', __name__)

def get_sentiment_stats(comments):
    sentiments = analyze_sentiment(comments)
    return {
        'mean': sum(sentiments) / len(sentiments) if sentiments else 0,
        'max': max(sentiments) if sentiments else 0,
        'min': min(sentiments) if sentiments else 0
    }

@blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_id = request.form['video_id']
        comments = fetch_comments(video_id)
        sentiment_stats = get_sentiment_stats(comments)
        return render_template('results.html', stats=sentiment_stats)
    return render_template('index.html')
