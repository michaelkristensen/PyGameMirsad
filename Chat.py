from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")



while (True):
    textToChat = input('Ask something')
    textFromChat = chatbot.get_response("textToChat")
    print(textFromChat)