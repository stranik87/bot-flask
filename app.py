from flask import Flask, request
from telegram import Bot
import os

TOKEN = os.environ.get('TOKEN')

app = Flask(__name__)

bot = Bot(token=TOKEN)


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World'
    elif request.method == 'POST':
        update = request.get_json()
        chat_id = update['message']['chat']['id']
        text = 'Salom'
        
        bot.send_message(chat_id=chat_id,text=text)
  
        return ' Go POST requests'
    
