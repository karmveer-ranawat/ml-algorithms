import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the required lexicon
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    scores = sid.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Get user input
text = input("Enter the text: ")  # Fixed input function syntax

# Analyze sentiment
sentiment = analyze_sentiment(text)

# Print result
print("Sentiment:", sentiment)
