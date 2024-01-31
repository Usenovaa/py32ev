import telebot
import random

token = '6828111261:AAF5zEXvSC0VvpBVOCawDUgb5da5UM9oo1A'


bot = telebot.TeleBot(token)

# print(dir(bot))

# @bot.message_handler(commands=['start', 'py32', 'test'])
# def start_message(message):
#     # print(message)
#     bot.send_message(message.chat.id, 'Привет')
#     bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAELSb9lukRjqYKEfhxCGTVnQiC9jaRMGQAC5QkAAoez8VBLQse1bMwsKTQE')

keyboard = telebot.types.ReplyKeyboardMarkup()

button1 = telebot.types.KeyboardButton('Играть')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    answer = bot.send_message(message.chat.id, 'Привет, начнем игру?',reply_markup=keyboard)
    # print(answer)
    bot.register_next_step_handler(answer, check_answer)


def check_answer(answer):
    if answer.text == 'Играть':
        bot.send_message(answer.chat.id, 'Ураааааааа\nВам нужно угадать число, у вас 3 попытки')
        random_number = random.choice(range(1, 11))
        print(random_number)
        game(answer, 3, random_number)
    else:
        bot.send_message(answer.chat.id, 'Пока')


def game(message, attempts, random_number):
    answer = bot.send_message(message.chat.id, 'Выберите число от 1 до 10')
    bot.register_next_step_handler(answer, check_number, attempts-1, random_number)


def check_number(answer, attempts, random_number):
    if answer.text == str(random_number):
        bot.send_message(answer.chat.id, 'Вы победили!')

    elif attempts == 0:
        bot.send_message(answer.chat.id, 'У вас закончились попытки')

    else:
        bot.send_message(answer.chat.id, f'Попробуйте еще раз, у вас {attempts} попыток')
        game(answer, attempts, random_number)
   

bot.polling()

