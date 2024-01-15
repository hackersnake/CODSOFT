import re
import random
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define rules and responses
rules = [
    {"pattern": r"hello|hi|hey", "responses": ["Hi there! How can I assist you today?", "Hello!"]},
    {"pattern": r"how are you", "responses": ["I'm just a chatbot, but thanks for asking!"]},
    {"pattern": r"bye|goodbye", "responses": ["Goodbye! Have a great day!", "See you later!"]},
    {"pattern": r"help", "responses": ["Sure, I'm here to help. Ask me anything!", "How can I assist you?"]},
    {"pattern": r"your name", "responses": ["I'm ChatBot, created by Shon Gaikwad."]},
    {"pattern": r"(.*)", "responses": ["I'm sorry, I didn't understand that. Can you provide more details?"]},
]

def respond_to_user_input(user_input):
    # Process user input using spaCy
    doc = nlp(user_input)

    # Check for pattern matches
    for rule in rules:
        if re.search(rule["pattern"], user_input):
            return random.choice(rule["responses"])

# Example usage
def main():
    while True:
        user_query = input("You: ")
        if user_query.lower() == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        response = respond_to_user_input(user_query)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
