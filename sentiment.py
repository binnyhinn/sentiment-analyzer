import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    
    if score['compound'] >= 0.05:
        sentiment = "Positive 😊"
    elif score['compound'] <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    print(f"Sentiment: {sentiment}")
    print(f"Score: {score}")
    print("---")

print("=== Sentiment Analyzer ===")
print("Type any sentence and I will tell you if it is positive, negative or neutral.")
print("Type 'quit' to exit.")
print("")

while True:
    text = input("Enter text: ")
    if text.lower() == "quit":
        print("Goodbye!")
        break
    analyze_sentiment(text)