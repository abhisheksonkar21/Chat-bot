import nltk
from nltk.chat.util import Chat

pairs = [
    ["hello", "Hi there! How can I help you today?"],
    ["what is your name", "My name is Chatbot."],
    ["how are you", "I'm doing well, thank you."],
    ["goodbye", "Goodbye! Have a nice day."]
]

chat = Chat(pairs, reflections=["I", "you", "me", "my"])
chat.converse()