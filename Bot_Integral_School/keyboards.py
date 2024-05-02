from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from random import choice


def random_back():
    return choice(['Назад'])


admin_panel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить сообщение')], [KeyboardButton(text='Список пользователей')],
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

user_sms = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Написать Maria_Malashta')], [KeyboardButton(text='Написать Sofi_Leuhina')],
    [KeyboardButton(text='Написать USER_3')], [KeyboardButton(text='Написать USER_4')],
    [KeyboardButton(text='Написать NasimLat')], [KeyboardButton(text='Написать Anastasia_Borodina')],
    [KeyboardButton(text='Написать всем пользователям')], [KeyboardButton(text='Вернутся в админ панель')]

],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню после команды /start
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание')], [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Доп. занятия')], [KeyboardButton(text='Подготовка к зачетам')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


user_plys = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Доп. занятия')], [KeyboardButton(text='Подготовка к зачетам')],
    [KeyboardButton(text='Случайное число')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню на кнопку Информация
info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О боте')],
    [KeyboardButton(text='Связь с администратором')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

# меню на кнопку Расписание
# todo Пример того, как можно оформлять клавиатуру по несколько кнопок в строке
sche = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='8А'), KeyboardButton(text='8Б')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню на кнопку Доп. занятия
addclass = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Дополнительные уроки')], [KeyboardButton(text='Секции')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

# меню на кнопку Доп уроки в разделе Доп. занятия
dop_yrok = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Доп. уроки по физике1')], [KeyboardButton(text='Доп. уроки по химии2')],
    [KeyboardButton(text='Доп. уроки по русскому языку3')],
    [KeyboardButton(text='Доп. уроки по математике4')], [KeyboardButton(text='Доп. уроки по история5')],
    [KeyboardButton(text='Доп. уроки по обществознанию6')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню на кнопку Другое
other = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')]
    ])

# меню на кнопку Связь с администратором и на команду /hadm
help_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/Kostaborodin')],
    [InlineKeyboardButton(text='VK', url='https://vk.com/id659392062')]
    ])


student = ['биба', 'боба', 'вова', 'коля', 'володя', 'сергей']


async def inline_student():
    keyboard = InlineKeyboardBuilder()
    for car in student:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/'))
    return keyboard.adjust(2).as_markup()


# кнопка подготовка к зачетам
vopros = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='По русскому языку')], [KeyboardButton(text='По физике')],
    [KeyboardButton(text='Назад')],
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros_ryss = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 1')], [KeyboardButton(text='Вопрос 2')], [KeyboardButton(text='Вопрос 3')],
    [KeyboardButton(text='Вопрос 4')], [KeyboardButton(text='Вопрос 5')], [KeyboardButton(text='Вопрос 6')],
    [KeyboardButton(text='Вопрос 7')], [KeyboardButton(text='Вопрос 8')], [KeyboardButton(text='Вопрос 9')],
    [KeyboardButton(text='Вопрос 10')], [KeyboardButton(text='Вопрос 11')], [KeyboardButton(text='Вопрос 12')],
    [KeyboardButton(text='Вопрос 13')], [KeyboardButton(text='Вопрос 14')], [KeyboardButton(text='Вопрос 15')],
    [KeyboardButton(text='Вопрос 16')], [KeyboardButton(text='Вопрос 17')], [KeyboardButton(text='Вопрос 18')],
    [KeyboardButton(text='Вопрос 19')], [KeyboardButton(text='Вопрос 20')], [KeyboardButton(text='Вопрос 21')],
    [KeyboardButton(text='Вопрос 22')], [KeyboardButton(text='Вопрос 23')], [KeyboardButton(text='Вопрос 24')],
    [KeyboardButton(text='Вопрос 25')], [KeyboardButton(text='Вопрос 26')], [KeyboardButton(text='Вопрос 27')],
    [KeyboardButton(text='Вопрос 28')], [KeyboardButton(text='Вопрос 29')], [KeyboardButton(text='Вопрос 30')],
    [KeyboardButton(text='Вопрос 31')], [KeyboardButton(text='Вопрос 32')], [KeyboardButton(text='Вопрос 33')],
    [KeyboardButton(text='Вопрос 34')], [KeyboardButton(text='Вопрос 35')], [KeyboardButton(text='Вопрос 36')],
    [KeyboardButton(text='Вопрос 37')], [KeyboardButton(text='Вопрос 38')], [KeyboardButton(text='Вопрос 39')],
    [KeyboardButton(text='Вопрос 40')], [KeyboardButton(text='Вопрос 41')], [KeyboardButton(text='Вопрос 42')],
    [KeyboardButton(text='Вопрос 43')], [KeyboardButton(text='Вопрос 44')], [KeyboardButton(text='Вопрос 45')],
    [KeyboardButton(text='Вопрос 46')], [KeyboardButton(text='Вопрос 47')], [KeyboardButton(text='Вопрос 48')],
    [KeyboardButton(text='Вопрос 49')], [KeyboardButton(text='Вопрос 50')], [KeyboardButton(text='Вопрос 51')],
    [KeyboardButton(text='Вопрос 52')], [KeyboardButton(text='Вопрос 53')], [KeyboardButton(text='Вопрос 54')],
    [KeyboardButton(text='Вопрос 55')], [KeyboardButton(text='Вопрос 56')], [KeyboardButton(text='Назад')],
    [KeyboardButton(text='Случайные 3 вопроса')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Назад'), KeyboardButton(text='Вопрос 2')],
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

vopros2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 1'), KeyboardButton(text='Вопрос 3')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros3 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 2'), KeyboardButton(text='Вопрос 4')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros4 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 3'), KeyboardButton(text='Вопрос 5')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros5 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 4'), KeyboardButton(text='Вопрос 6')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros6 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 5'), KeyboardButton(text='Вопрос 7')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros7 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 6'), KeyboardButton(text='Вопрос 8')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros8 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 7'), KeyboardButton(text='Вопрос 9')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros9 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 8'), KeyboardButton(text='Вопрос 10')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros10 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 9'), KeyboardButton(text='Вопрос 11')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros11 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 10'), KeyboardButton(text='Вопрос 12')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros12 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 11'), KeyboardButton(text='Вопрос 13')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros13 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 12'), KeyboardButton(text='Вопрос 14')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros14 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 13'), KeyboardButton(text='Вопрос 15')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros15 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 14'), KeyboardButton(text='Вопрос 16')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros16 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 15'), KeyboardButton(text='Вопрос 17')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros17 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 16'), KeyboardButton(text='Вопрос 18')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros18 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 17'), KeyboardButton(text='Вопрос 19')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros19 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 18'), KeyboardButton(text='Вопрос 20')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros20 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 19'), KeyboardButton(text='Вопрос 21')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros21 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 20'), KeyboardButton(text='Вопрос 22')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros22 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 21'), KeyboardButton(text='Вопрос 23')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros23 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 22'), KeyboardButton(text='Вопрос 24')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros24 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 23'), KeyboardButton(text='Вопрос 25')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros25 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 24'), KeyboardButton(text='Вопрос 26')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros26 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 25'), KeyboardButton(text='Вопрос 27')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros27 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 26'), KeyboardButton(text='Вопрос 28')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros28 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 27'), KeyboardButton(text='Вопрос 29')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

vopros29 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 28'), KeyboardButton(text='Вопрос 30')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros30 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 29'), KeyboardButton(text='Вопрос 31')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros31 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 30'), KeyboardButton(text='Вопрос 32')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros32 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 31'), KeyboardButton(text='Вопрос 33')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros33 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 32'), KeyboardButton(text='Вопрос 34')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros34 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 33'), KeyboardButton(text='Вопрос 35')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros35 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 34'), KeyboardButton(text='Вопрос 36')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros36 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 35'), KeyboardButton(text='Вопрос 37')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros37 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 36'), KeyboardButton(text='Вопрос 38')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros38 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 37'), KeyboardButton(text='Вопрос 39')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros39 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 38'), KeyboardButton(text='Вопрос 40')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros40 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 39'), KeyboardButton(text='Вопрос 41')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros41 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 40'), KeyboardButton(text='Вопрос 42')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

vopros42 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 41'), KeyboardButton(text='Вопрос 43')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros43 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 42'), KeyboardButton(text='Вопрос 44')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros44 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 43'), KeyboardButton(text='Вопрос 45')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros45 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 44'), KeyboardButton(text='Вопрос 46')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros46 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 45'), KeyboardButton(text='Вопрос 47')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros47 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 46'), KeyboardButton(text='Вопрос 48')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros48 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 47'), KeyboardButton(text='Вопрос 49')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros49 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 48'), KeyboardButton(text='Вопрос 50')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros50 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 49'), KeyboardButton(text='Вопрос 51')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros51 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 50'), KeyboardButton(text='Вопрос 52')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros52 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 51'), KeyboardButton(text='Вопрос 53')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros53 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 52'), KeyboardButton(text='Вопрос 54')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros54 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 53'), KeyboardButton(text='Вопрос 55')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

vopros55 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 54'), KeyboardButton(text='Вопрос 56')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


vopros56 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 55')],
    [KeyboardButton(text='Меню вопросов по русскому языку')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')
