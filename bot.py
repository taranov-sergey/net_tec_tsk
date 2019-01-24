import telebot
import wikipedia
# from telebot import apihelper
                   
TOKEN = '111111111:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# telebot.apihelper.proxy = {'https': "https://94.130.98.54:8888"}
# apihelper.proxy = {'https': "https://176.114.8.81:65233"}
# bot = telebot.TeleBot(token=TOKEN)
bot = telebot.TeleBot(TOKEN)
d = {'afafafaf': 'af * 4'}
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)
INFO = 'full info :)'
START = "To start use this bot see command list via command /command_list"
HELP = "This is telegram bot that can send you summary part of wikipedia article for your message"
AUTHOR = 'this bot has been created by Sergey Taranov group 573'
COMMAND_LIST = "/help - see help message\n" \
                 '/start - see start message\n'\
                 '/command_list - see command list\n'\
                 '/info - see full info about bot\n'\
                 '/author - see author info\n'\
                 '/summary or /s - see summary of wikipedia article\n'\
                 '/article_url or /u - see url of Wikipedia article\n'\
                 '/chat_id - see chat_id\n'\
                 '/storage - see titels that are in storage at this moment'

@bot.message_handler(commands=['help'])
def answer(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=HELP
    )
    
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=START
    )
    
@bot.message_handler(commands=['command_list'])
def send_command_list(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=COMMAND_LIST
    )

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=INFO
    )
    
@bot.message_handler(commands=['author'])
def send_author(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=AUTHOR
    )

@bot.message_handler(commands=['storage'])
def send_author(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=d.keys()
    )
    
# @bot.message_handler(commands=['summary', 's'])
@bot.message_handler()
def send_summary(message):
#     print('summary text')
#     title = ''.join(message.text.split(" ")[1:])
    title = message.text
#     if title == '_ubivca':
#         bot.stop_polling()
    try:
        summary = wikipedia.summary(title=title)
        d[title] = summary
    except:
        if title in d.keys():
            summary = d[title]
            summary = 'In Wikipedia there is not any pages with title "%s"' % title + \
                    ' but summary of this article is in bot storage\n%s' % summary
        else:
            summary = 'In Wikipedia there is not any pages with title %s' % title
    bot.send_message(
        chat_id=message.chat.id,
        text = summary
    )

    
    
@bot.message_handler(commands=['chat_id'])
def send_chat_id(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.chat.id
    )
    
@bot.message_handler(commands=['article_url','u'])
def send_welcome(message):
#     print('summary text')
    title = ''.join(message.text.split(" ")[1:])
    try:
        page = wikipedia.WikipediaPage(title=title)
        url = page.url
    except:
        url = 'In Wikipedia there is not any pages with title %s' % title
    bot.reply_to(message, text=url)

# bot.get_me()
# bot.send_message(chat_id=284239137, text='hi')
bot.polling(interval=15)
