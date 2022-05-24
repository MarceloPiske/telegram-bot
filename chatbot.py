from time import sleep
from PiskeBot import PiskeBot
import os


token = "5118934706:AAGLR_5ShWZcFApQkcLsioPEh_0IbfHvYd8"
print(token)

while True:

    # Função encarregada de ouvir novas mensagens
    my_bot = PiskeBot(token)
    have_news = my_bot.listener_messages()

    if have_news:
        print(have_news)
    my_bot.send_message(5302085872, "Hello")
    sleep(3)
