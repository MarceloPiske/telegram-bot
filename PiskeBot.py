import requests
import json
from datetime import datetime
import os

class PiskeBot:
    def __init__(self, token):
        self.token = token
    
    def listener_messages(self):
        # Rotorna novas mensagens caso encontre.
        have_news = False
        request = json.loads(requests.get(
            f'https://api.telegram.org/bot{self.token}/getUpdates'
        ).text)
        # Se a posição é diferente existe uma nova mensagem
        result = request['result']

        if result:
            new_update = result[len(result)-1]['update_id']
            last_update = int(os.environ.get('UPDATE_ID')) if os.environ.get('UPDATE_ID') else os.environ.get('UPDATE_ID')
            if last_update:
                if last_update < new_update:
                    os.environ['UPDATE_ID'] = str(new_update)

                    have_news = True
            else:
                os.environ['UPDATE_ID'] = str(new_update)

                have_news = True

        return have_news

    def return_chat_details():
        request = json.loads(requests.get(
            f'https://api.telegram.org/bot{token}/getUpdates'
        ).text)
        
        result = request['result']

        message_text = result[len(result)-1]['message']['text']
        message_chat = result[len(result)-1]['message']['chat']
        message_date = result[len(result)-1]['message']['date']
        message_date = datetime.fromtimestamp(message_date)

    def send_message(self, chat_id, message):
        
        req = requests.get(
            f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
        )
        
        print(req.text)
