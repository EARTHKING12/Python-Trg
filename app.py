from transformers import pipeline

#Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

#take input from user
text = input("Enter a sentence : ")
#Analyze sentiment
result = sentiment_analyzer(text)

print(result[0]['label'])
print(result[0]['score'])
# print(result)