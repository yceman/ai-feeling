from textblob import TextBlob

text = "I love learning new things!"
sentiment = TextBlob(text).sentiment.polarity

if sentiment > 0:
    print("AI feels happy 😊")
elif sentiment < 0:
    print("AI feels sad 😢")
else:
    print("AI feels neutral 😐")

