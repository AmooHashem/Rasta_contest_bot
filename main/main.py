from telegram import KeyboardButton, ReplyKeyboardMarkup, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackQueryHandler
import requests
import re

my_token = '996901425:AAHeL5pN03vZZ2KouvIMbuhyJq4YrpRH3tI'


# def add_team(bot, update, cursor, num, name):
#     cursor.execute('insert into teams values (?,?,?)', num, name, 0)


def start(update, context):
    keyboard = [[InlineKeyboardButton("افزودن تیم", callback_data='add_team'),
                 InlineKeyboardButton("حذف تیم", callback_data='delete_team')],
                [InlineKeyboardButton("افزودن سوال", callback_data='add_question'),
                 InlineKeyboardButton("حذف سوال", callback_data='delete_question')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot = update.message.bot
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='یکی از گزینه های زیر رو انتخاب کنید:', reply_markup=reply_markup)


def admin_buttons(update, context):
    query = update.callback_query

    query.edit_message_text(text='لطفا شماره ی تیم را وارد کنید.')


def main():
    updater = Updater(my_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(admin_buttons))
    # dp.add_handler(CommandHandler('Add team', add_team))
    # dp.add_handler(CommandHandler('Delete team', del_team))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
