import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai

updater = Updater("1244003572:AAEeygp2pIqS3M56jS0TeXkfawOQqor2gkA", use_context=True)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, давай пообщаемся?")


def textMessage(bot, update):
    request = apiai.ApiAI("2fb84f1a921a4bb3bdb1d053cb19d012").text_request()
    request.lang = "ru"
    request.session_id = "mansocbot"
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode("utf-8"))
    response = responseJson["result"]["fulfillment"]["speech"]
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Я Вас не совсем понял!")


start_command_handler = CommandHandler("start", startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
