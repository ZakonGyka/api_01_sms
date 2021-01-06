import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# from twilio.com/console
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
API_VK = 'https://api.vk.com/method/'

client_twilio = Client(ACCOUNT_SID, AUTH_TOKEN)


def get_status(user_id):
    print('+')

    params = {
        "fields": "online",
        "user_ids": user_id,
        "v": "5.92",
        "access_token": ACCESS_TOKEN,
    }
    user_information = requests.post(
        f'{API_VK}/users.get',
        params=params
    )
    return user_information.json()['response'][0]['online']


def sms_sender(sms_text):
    message = client_twilio.messages.create(
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO'),
        body=sms_text)
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == '__main__':
    vk_id = os.getenv('VK_ID')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
