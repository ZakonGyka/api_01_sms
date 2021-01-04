import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)


def get_status(user_id):
    access_token = os.getenv('access_token')
    params = {
        "fields": "online",
        "user_ids": user_id,
        "v": "5.92",
        "access_token": access_token,
    }
    user_information = requests.post('https://api.vk.com/method/users.get', params=params)
    return user_information.json()['response'][0]['online']


def send_sms(sms_text):
    message = client.messages.create(
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO'),
        body=sms_text)
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == '__main__':
    vk_id = 20316432
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
