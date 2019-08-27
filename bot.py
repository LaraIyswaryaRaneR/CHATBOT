from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Test')
trainer = ListTrainer(bot)

for files in os.listdir('D:/New folder (2)/'):
    conversation = open('D:/New folder (2)/' + files, 'r').readlines()
    trainer.train(conversation)

while True:
    request = input('You:').lower()
    response = bot.get_response(request)
    print('Botish:', response)
