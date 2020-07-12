""" Бот для поиска информации на википедии по запросу пользователя.
Если информация найдена возвращает текст статьи с википедии.
"""


from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
from texts import *
import wikipediaapi


lang = 'ru'

bot = TeleBot(TOKEN)
wiki = wikipediaapi.Wikipedia('ru', extract_format=wikipediaapi.ExtractFormat.WIKI)


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(*[KeyboardButton(text=text) for text in LANGUAGE.keys()])

    bot.send_message(message.chat.id, 'Выберите язык', reply_markup=kb)


@bot.message_handler(content_types=['text'], func=lambda message: message.text in LANGUAGE.keys())
def set_language(message):
    global lang
    lang = LANGUAGE[message.text]
    global wiki
    wiki = wikipediaapi.Wikipedia(LANGUAGE[message.text], extract_format=wikipediaapi.ExtractFormat.WIKI)

    txt = FIND_TEXT[LANGUAGE[message.text]]
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text'],
                     func=lambda message: message.text not in [val[1] for val in FIND_ELSE_KB.values()])
def find_info(message):

    page = wiki.page(message.text)

    def split_text(sections, level=0):
        text = []

        def split_section(sec, i=0):
            subtext = sec.text.split('\n')
            txt = []

            while len(subtext) != 0:
                for p in subtext:
                    if len(p) < 4096 and len(txt) == 0:
                        txt.append([subtext.pop(0)])
                    elif len(txt[i][0]) + len(p) < 4096:
                        txt[i].append(subtext.pop(0))
                    else:
                        for el in split_section(subtext, i + 1):
                            txt.append(el)
            return txt

        for s in sections:
            if len(s.text) < 4096:
                text.append("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:]))
            else:
                for par in [el for el in split_section(s)]:
                    if type(par) != list:
                        text.append(par)
                    else:
                        text.extend(par)
            for el in split_text(s.sections, level + 1):
                text.append(el)
        return text

    if page.exists():
        mes_text = split_text(page.sections)
        while '' in mes_text:
            mes_text.remove('')
    else:
        mes_text = [NOT_FOUND[lang]]

    for section in mes_text:
        bot.send_message(message.chat.id, section)

    kb = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(ans, callback_data=f'find_else-{ans}') for ans in FIND_ELSE_KB[lang]]
    kb.add(*buttons)
    bot.send_message(message.chat.id, FIND_MORE[lang], reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'find_else')
def find_else(call):
    if call.data.split('-')[1] in [ans[0] for ans in FIND_ELSE_KB.values()]:
        txt = FIND_TEXT[lang]
    elif call.data.split('-')[1] in [ans[1] for ans in FIND_ELSE_KB.values()]:
        txt = GOOD_BYE[lang]
    # bot.delete_message(call.massge.chat.id, call.massage.message_id)
    # bot.send_message(call.massega.chat.id, txt)
    bot.edit_message_text(txt, call.message.chat.id, call.message.message_id)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling()
