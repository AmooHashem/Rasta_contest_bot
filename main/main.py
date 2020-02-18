import sqlite3

from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

my_token = '996901425:AAHeL5pN03vZZ2KouvIMbuhyJq4YrpRH3tI'
conn = sqlite3.connect('bot.db')
c = conn.cursor()
c.execute('create table users (chat_id int,state string);')
c.execute('create table teams (number int,name string,score real);')


def start(update, context):
    bot = update.message.bot
    message = update.message

    print(message.chat_id)
    print(type(message.chat_id))
    # add user to database
    c.execute('insert into users values ({},{});'.format(message.chat_id, "\'menu\'"))

    print(":))")

    # show initial messages to user
    keyboard = [[KeyboardButton("Change score"), KeyboardButton("Assign problem")],
                [KeyboardButton("Suspend a team"), KeyboardButton("Show team solved problems")],
                [KeyboardButton("Show team in-hand problems")]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        'سلام منتور عزیز!\nخسته نباشی!\nایشالا مسابقه ی خوبی در پیش داشته باشیم!\n', reply_markup=reply_markup)


def admin(update, context):
    bot = update.message.bot
    message = update.message

    # change state of user to "admin" mode
    c.execute("update users set state = {} where chat_id = {}".format("\'admin\'", message.chat_id))

    keyboard = [[KeyboardButton("Add team"), KeyboardButton("Delete team")],
                [KeyboardButton("Add question"), KeyboardButton("Delete question")]]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.send_message(chat_id=message.chat_id, text='سلام ادمین!\nیکی از گزینه های زیر رو انتخاب کن:',
                     reply_markup=reply_markup)


def messages(update, context):
    bot = update.message.bot
    message = update.message

    state = c.execute("select state from users where chat_id = {}".format(message.chat_id)).fetchall()[0][0]

    print(state + "???????????????????????")

    if state == "افزودن تیم":
        bot.send_message(":)")
    if state == "delete_team":
        pass
    if state == "add_question":
        pass
    if state == "delete_question":
        pass


def main():
    updater = Updater(my_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, messages))

    # dp.add_handler(CommandHandler('Add team', add_team))
    # dp.add_handler(CommandHandler('Delete team', del_team))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
