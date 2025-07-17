# app.py

from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

print("Welcome to the Mental Health Support Chatbot!")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Take care. You're not alone.")
        break
    result = classifier(user_input)[0]
    emotion = result['label']
    print(f"Chatbot (Emotion: {emotion}): I'm here for you. Want to try a deep breathing exercise?")
