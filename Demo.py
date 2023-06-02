# create a chatbot instance
from chatterbot import ChatBot
def create_chatbot(name, **kwargs):
    chatbot = ChatBot(name, **kwargs)
    return chatbot

# create a chatbot instance
chatbot = create_chatbot('Test')
chatbot.train('chatterbot.corpus.english')
# create a chatbot instance
chatbot = create_chatbot('Test',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
# create a chatbot instance
# chatbot = create_chatbot('Test')
