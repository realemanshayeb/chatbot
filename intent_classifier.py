#intent_classifier.py

from transformers import pipeline 

#load zero-shot classifier

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") 

labels = ["technical issue", "billing problem", "refund reqest", "new account", "cancel subscription", "unclear"]

response_map = {
    "technical issue": "Let's get that fixed. What device or service are you having issues with?",
    "billing problem": "I understand you have a billing concern. Can you share more details or your invoice number?",
    "refund request": "I'm happy to help with a refund. Can you provide the order ID?",
    "new account": "That's amazing! Which account are you looking to open with us?",
    "cancel subscription": "I'm sorry to see you go. Would you like help canceling your subscription now?",
    "unclear": "Could you please clarify your request?",
    "unrelated": "Is this request related to a customer support concern?"
}
def classify_intent(text):
    result = classifier(text, candidate_labels = labels)
    intent = result["labels"][0]  # top prediction
    response = response_map.get(intent, "I'm here to help. Could you clarify your request?")
    return intent, response