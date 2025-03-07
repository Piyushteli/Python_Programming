"""
Implementing a Chatbot using python.
"""
import random

# Define a dictionary with intents and responses
intents = {
    'hello': ['Hi, how are you?', 'Hello! How can I assist you?'],
    'I am fine':["That's good! How can I assist you?"],
    'how are you': ['I\'m doing great, thanks!', 'I\'m good, thanks for asking!'],
    'what is your name': ['My name is ChatBot!', 'I\'m an AI chatbot, nice to meet you!'],
    'default': ['Sorry, I didn\'t understand that.', 'Can you please rephrase?']
}

def chatbot(message):
    message = message.lower()
    for intent, responses in intents.items():
        if intent in message:
            return random.choice(responses)
    return random.choice(intents['default'])

def main():
    print("Welcome to the chatbot!")
    while True:
        message = input("You: ")
        if message.lower() == 'quit':
            break
        response = chatbot(message)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
