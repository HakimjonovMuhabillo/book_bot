from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram.utils.callback_data import CallbackData

def generate_start_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Начать бронирование')
    markup.add(btn)
    return markup




one_people = InlineKeyboardButton(text='1 человек', callback_data='one_people')
two_people = InlineKeyboardButton(text='2 человек', callback_data='two_people')
three_people = InlineKeyboardButton(text='3 человек', callback_data='three_people')
four_people = InlineKeyboardButton(text='4 человек', callback_data='four_people')
markup_people = InlineKeyboardMarkup().add(one_people, two_people, three_people, four_people)



