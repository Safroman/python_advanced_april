"""1) Написать бота-консультанта, который будет собирать информацию с
пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
Записывать сформированную заявку в БД (по желанию SQl/NOSQL).)."""


import telebot
from .config import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from mongoengine import *


bot = telebot.TeleBot(TOKEN)
data = {}
connect('bot_db')


class User(Document):

    surname = StringField(required=True)
    name = StringField(required=True)
    middle_name = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    address = StringField(required=True)
    wishes = StringField(required=True)


@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Да', callback_data='yes')
    button2 = InlineKeyboardButton('Нет', callback_data='no')
    kb.add(button1, button2)

    bot.send_message(message.chat.id, 'Здравствуйте. Пройдете опрос?', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'no')
def bye(call):
    bot.send_message(call.from_user.id, 'До свидания')


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def start(call):
    bot.send_message(call.from_user.id, 'Хорошо')
    bot.send_message(call.from_user.id, 'Как Вас зовут?')


@bot.message_handler(content_types=['text'])
def response(message):
    data['name'] = message.text
    bot.send_message(message.chat.id, 'Какая у Вас фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    data['surname'] = message.text
    bot.send_message(message.chat.id, 'Как Ваше отчество?')
    bot.register_next_step_handler(message, get_middle_name)


def get_middle_name(message):
    data['middle_name'] = message.text
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='поделиться контактом', request_contact=True)
    kb.add(button)
    bot.send_message(message.chat.id, 'Поделитесь номером телефона?', reply_markup=kb)
    bot.register_next_step_handler(message, get_phone)


@bot.message_handler(content_types=['contact'])
def get_phone(message):
    data['phone'] = message.contact.phone_number
    bot.send_message(message.chat.id, 'Какой у Вас e-mail?')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    data['email'] = message.text
    bot.send_message(message.chat.id, 'Какой Ваш адрес?')
    bot.register_next_step_handler(message, get_address)


def get_address(message):
    data['address'] = message.text
    bot.send_message(message.chat.id, 'Какие у Вас пожелания?')
    bot.register_next_step_handler(message, get_wishes)


def get_wishes(message):
    data['wishes'] = message.text
    User.objects.create(**data)
    bot.send_message(message.chat.id, 'Спасибо.')


bot.polling()
