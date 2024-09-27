from aiogram import executor, Dispatcher, Bot, types
from aiogram.types import Message, ReplyKeyboardRemove
from database import *
from state import Register
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboard import *

bot = Bot(token='7003776520:AAHlIQly8I9E7_Ss90Up4McNpJSwwuAAgpY')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def start_command(message: Message):
    chat_id = message.chat.id
    create_users_table()
    await bot.send_message(chat_id, 'Привет это бот для бронирования', reply_markup=generate_start_button())


@dp.message_handler(commands='cancel')
async def cancel_command(message: Message):
    chat_id = message.chat.id
    cancel_table()
    await bot.send_message(chat_id, 'Бронирование было отменено')


@dp.message_handler(commands='help')
async def help_command(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id,
                           'Для начала бронирования напишите /start. Для отмены бронирования напишите'
                           ' /cancel. Для просмотра заказанного столика напишите /booking')


@dp.message_handler(commands='booking')
async def booking_command(message: Message):
    chat_id = message.chat.id
    chat_id = int(chat_id)
    try:
        booking = get_booking(chat_id)
        await bot.send_message(chat_id, f'Вы бронировали на имя {booking[2]} на дату {booking[3]} на время {booking[4]}'
                                        f' на {booking[5]} человек')
    except Exception:
        await bot.send_message(chat_id, 'Вы еще не бронировали столик')


@dp.message_handler(regexp='Начать бронирование')
async def start_bron(message: Message):
    chat_id = message.chat.id
    await Register.name.set()
    await bot.send_message(chat_id, 'Введите вашу фамилию и имя', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=Register.name)
async def get_name_ask_date(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.update_data(name=message.text)
    await Register.date.set()
    await bot.send_message(chat_id, 'Выберите день,  формате "20/11/2000" ')


@dp.message_handler(state=Register.date, regexp='\d{1,2}\/\d{1,2}\/\d{2,4}')
async def get_date_ask_time(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.update_data(date=message.text)
    await Register.time.set()
    await bot.send_message(chat_id, 'Напишите время в формате  "HH:MM" ')


@dp.message_handler(state=Register.time, regexp='([01]?[0-9]|2[0-3]):[0-5][0-9]')
async def get_time_ask_number_of_people(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.update_data(time=message.text)
    await Register.number_of_people.set()
    await bot.send_message(chat_id, 'Сколько будет людей?')


@dp.message_handler(state=Register.number_of_people)
async def get_number_of_people_save_data(message: Message, state: FSMContext):
    chat_id = message.chat.id
    data = await state.get_data()
    number_of_people = message.text
    insert_data(chat_id, data['name'], data['date'], data['time'], number_of_people)
    await state.finish()
    await bot.send_message(chat_id, 'Вы удачно забронировали столик')


executor.start_polling(dp)
