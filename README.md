# API_sms_bot
Бот позволяющий следить за состоянием произвольного пользователя, в онлайне пользователь или в оффлайне. При появлении пользователя, который определяется по id, в сети, на указанный номер отправляется sms сообщение с что данный пользователь онлайн.
# Install
1. Клонировать проект
```Python
git clone https://github.com/ZakonGyka/api_01_sms.git
```
2. Создать новое вертуальное окружение
```Python
python -m venv env
```
3. Устноавить зависимости
```Python
pip install -r /path/to/requirements.txt
```
4. Запускить приложение
```Python
pip manage.py runserver
```
# Requirements
+ pyjwt==1.7.1
+ python-dotenv==0.12.0
+ twilio==6.35.5
