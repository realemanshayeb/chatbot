#intent_classifier.py

from transformers import pipeline 

#load zero-shot classifier

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") 

labels = ["technical issue", "billing problem", "refund reqest", "new account", "cancel subscription"]

def classify_intent(text):
    result = classifier(text, labels)
    return result["labels"][0]  # top prediction