"""
Simple Sentiment Analysis
"""

def sentiment_analysis(text):
    positive_words=["good","great","excellent","awesome","happy"]
    negative_words=["bad","terriable","awful","poor","sad"]

    text=text.lower()
    words=text.split()

    positive_count=sum(1 for word in words if word in positive_words)
    negative_count=sum(1 for word in words if word in negative_words)

    if positive_count>negative_count:
        return "Positive"
    elif negative_count>positive_count:
        return "Negative"
    else:
        return "Neutral"

text=input("Enter a text: ")
print(sentiment_analysis(text))