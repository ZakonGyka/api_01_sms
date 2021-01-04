import time

import requests
from twilio.rest import Client

# здесь проинициализируйте Client
# Your Account SID from twilio.com/console
account_sid = "AC6ae68f31f584a4c28bda6964a65e8b36"
# Your Auth Token from twilio.com/console
auth_token = "0f1c583706b7ea68dce7b7d9756e54d0"

client = Client(account_sid, auth_token)


def get_status(user_id):
    print('++++++++')
    params = {
        "user_id": user_id,
        "v": "5.92",
        "access_token": "a894afd651dea9c7036f4b41da2de35b027fa0b4314293d5869c1a870a77cc420d833f9f8367ffc1bcb12",
    }
    user_information = requests.post('https://api.vk.com/method/users.get?fields=online,status', params=params)
    return user_information.json()['response'][0]['online']
    # return ...  # Верните статус пользователя в ВК


# print(get_status(20316432))

def send_sms(sms_text):
    message = client.messages.create(
        to="+79774208055",
        from_="+15122706027",
        # media_url='https://demo.twilio.com/owl.png',
        body=sms_text)
    #print(message.sid)
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == '__main__':
    vk_id = 531301803
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
