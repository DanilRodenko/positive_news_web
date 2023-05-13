import requests
from nltk.sentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()
key = "ee82603e140342af8eb68c4119307ab0"
url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={key}"

request = requests.get(url)
content = request.json()

# Analyzer title. Get score
for article in content['articles']:
    scores = analyzer.polarity_scores(article['title'])
    article['score'] = dict(scores)

# Create positive news
positive_news = []

for pos_news in content['articles']:
    if pos_news['score']['pos'] > pos_news['score']['neg']:
        positive_news.append(pos_news)
    else:
        continue





