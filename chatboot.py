import nltk
import re
import random
import string

# Download the necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

# Sample responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hello", "I am glad! You are talking to me"]

# Sample corpus for responses
CORPUS = {
    'how are you': 'I am fine, thank you! How can I help you today?',
    'bye': 'Goodbye! Have a great day!',
    'what is your name': 'I am a chatbot created to assist you.',
    'thank you': 'You are welcome!',
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def generate_response(user_input):
    user_input = preprocess(user_input)
    
    # Check for greetings
    response = greeting(user_input)
    if response:
        return response
    
    # Default response if the input is not in the corpus
    return CORPUS.get(user_input, "I am sorry! I don't understand you.")

def chatbot():
    print("Chatbot: Hi there! I am your assistant. How can I help you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
