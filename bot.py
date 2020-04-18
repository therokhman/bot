import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai

updater = Updater(token="1244003572:AAEeygp2pIqS3M56jS0TeXkfawOQqor2gkA", use_context=True)
dp = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Хочешь пообщаться?")


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
        bot.send_message(chat_id=update.message.chat_id, text="Не понятно, что вы написали!")


dp.add_handler(CommandHandler("start", startCommand))
dp.add_handler(MessageHandler(Filters.text, textMessage))
updater.start_polling()
updater.idle()
