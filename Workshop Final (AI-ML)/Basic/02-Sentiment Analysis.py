# Natural Language Processing (NLP): Sentiment Analysis

from textblob import TextBlob

text = "I love this product!"
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f'Sentiment score: {sentiment}')
