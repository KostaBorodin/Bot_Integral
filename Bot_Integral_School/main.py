import asyncio
import string
import random
from config import *

from random import choice
from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import keyboards as kb
import text_handlers as t
from default_commands import *


bot = Bot(token=TOKEN)
dp = Dispatcher()

# todo Убрать все лишнее


class Reg(StatesGroup):
    name = State()
    number = State()
    help_test = State()
    sms_user_all = State()
    sms_user_Maria_Malashta = State()
    sms_user_Sofi_Leuhina = State()
    sms_user_USER_3 = State()
    sms_user_USER_4 = State()
    sms_user_NasimLat = State()
    sms_user_Anastasia_Borodina = State()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.id in (ID_USER_Maria_Malashta, ID_USER_Sofi_Leuhina):
        await message.answer(text=t.text_command_start(message),
                             reply_markup=kb.user_plys)
    else:
        await message.answer(text=t.text_command_start(message),
                             reply_markup=kb.main)
    await bot.send_message(ID_ADMIN, (f'В Botintegral зашел пользователь \n{message.from_user.first_name} ' 
                                      f'{message.from_user.last_name}\nID: {message.from_user.id}'))


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=t.text_command_help())


@dp.message(Command('hadm'))
async def cmd_h_adm(message: Message):
    await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
                               caption='Нам очень жаль, что вы столкнулись с ошибкой в боте,'
                                       ' просим вас сообщить о поблеме в личном сообщении нашему администратору.\n'
                                       '⬇️⬇️⬇️',
                               reply_markup=kb.help_admin)


@dp.message(Command('ry8b'))
async def ry_klassb(message: Message):
    id_photo = 'AgACAgIAAxkBAAJFP2Xy_XJtKhRXfyI5PZ1EZvEb4WdzAALv1jEbXECZS81ADCRjhTE5AQADAgADeQADNAQ'
    await message.answer_photo(photo=id_photo,
                               caption='Расписание уроков 8Б класс\n\n\n'
                                       'Понедельник:\n'
                                       '[8:30 - 9:10]    Разговоры о важном\n[9:20 - 10:00]  Физика\n'
                                       '[10:10 - 10:50]История России\n[11:15 - 11:55]Алгебра\n'
                                       '[12:20 - 13:00]География\n[13:15 - 13:55]Русский язык.\n\n'
                                       'Вторник:\n[8:30 - 9:10]Геометрия\n'
                                       '[9:20 - 10:00]Геометрия\n[10:10 - 10:50]Алгебра\n'
                                       '[11:15 - 11:55]Обществознание\n[12:20 - 13:00]Физкультура\n'
                                       '[13:15 - 13:55]Иностранный язык\n[14:05 - 14:45]Классный час.\n\n'
                                       'Среда:\n[9:20 - 10:00]История Россиии\n'
                                       '[10:10 - 10:50]Физика\n[11:15 - 11:55]Химия\n'
                                       '[12:20 - 13:00]Алгебра\n[13:15 - 13:55]Музыка\n'
                                       '[14:05 - 14:45]Иностранный язык\n\n'
                                       'Четверг:\n[8:30 - 9:10]География\n[9:20 - 10:00]Литература\n'
                                       '[10:10 - 10:50]ОПД\n[11:15 - 11:55]Физкультура\n[12:22 - 13:00]Алгебра\n\n'
                                       'Пятница:\n[8:30 - 9:10]Технология\n[9:20 - 10:00]Русский язык\n'
                                       '[10:10 - 10:50]Биолгия\n[11:15 - 11:55]Физкультура\n'
                                       '[12:20 - 13:00]Информатика\n\n'
                                       'Суббота:\n[8:30 - 9:10]Биология\n[9:20 - 10:00]Иностранный язык\n'
                                       '[10:10 - 10:50]Химия\n[11:15 - 11:55]Русский язык\n'
                                       '[12:20 - 13:00]Литература\n[13:15 - 13:55]ОБЖ.')

'''
@dp.message()
async def messages_handler(message: Message):
    get_message_bot = ' '.join(message.text.lower().split()).strip()
    get_message_bot = get_message_bot.translate(str.maketrans('', '', string.punctuation))
'''


@dp.message(F.text.lower() == 'случайное число')
async def schedule(message: Message):
    await message.answer("Ваше число: " + str(random.randint(0, 1000)))


@dp.message(F.text.lower() == 'расписание')
async def schedule(message: Message):
    await message.answer('Открываю расписания', reply_markup=kb.sche)


@dp.message(F.text.lower() == '8б')
async def schedule(message: Message):
    await message.answer_photo(
            photo='AgACAgIAAxkBAAJFP2Xy_XJtKhRXfyI5PZ1EZvEb4WdzAALv1jEbXECZS81ADCRjhTE5AQADAgADeQADNAQ',
            caption=t.text_ry8b())


@dp.message(F.text.lower() == '8а')
async def schedule(message: Message):
    await message.answer('Расписаие 8А класса еще не появилось')


@dp.message(F.text.lower() == 'информация')
async def schedule(message: Message):
    await message.answer('Открываю пунтк Информация', reply_markup=kb.info)


@dp.message(F.text.lower() == 'о боте')
async def schedule(message: Message):
    await message.answer(t.text_o_bot())


@dp.message(F.text.lower() == 'связь с администратором')
# async def schedule(message: Message):
#    await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
#                               caption=t.text_help_admin(),
#                               reply_markup=kb.help_admin)
async def reg_help(message: Message, state: FSMContext):
    await state.set_state(Reg.help_test)
    await message.answer('Пожалуста напишите о вашей проблеме, наш администратор в течение'
                         ' 24 часов разберётся в вашей жалобе', reply_markup=kb.other)


@dp.message(Reg.help_test)
async def reg_help_test(message: Message, state: FSMContext):
    await state.update_data(help_test=message.text)
    data = await state.get_data()
    await message.answer('Спасибо за обращение, мы вам ответим в течение 24 часов.', reply_markup=kb.main)
    await bot.send_message(ID_ADMIN, (f'Поступила жалоба от пользователя {message.from_user.last_name}'
                                      f' {message.from_user.first_name} \nпод ID: {message.from_user.id}'
                                      f' \n\n\nЖалоба: \n{data["help_test"]}'))
    await state.clear()


@dp.message(F.text.lower() == 'доп. занятия')
async def schedule(message: Message):
    await message.answer('Открываю пункт Дополнительные занятия', reply_markup=kb.addclass)


@dp.message(F.text.lower() == 'дополнительные уроки')
async def schedule(message: Message):
    await message.answer('Открываю пункт Дополнительные уроки', reply_markup=kb.dop_yrok)

# todo Добавить обработчки для команд шаг назад
# elif get_message_bot in ('назад', 'отменить', 'шаг назад', 'предыдущий', '⬅️'):
# await message.answer('◀️Назад', reply_markup=kb.main)


@dp.message(F.text.lower() == 'student')
async def how_are_you(message: Message):
    await message.answer('Ок!', reply_markup=await kb.inline_student())


@dp.message(F.text.lower() == 'Секции')
async def schedule(message: Message):
    await message.answer('Эта кнопка на этапе разработки')


@dp.message(F.text.lower() == 'подготовка к зачетам')
async def schedule(message: Message):
    await message.answer('Открываю меню: Подготовка к зачетам', reply_markup=kb.vopros)


@dp.message(F.text.lower() == 'по русскому языку')
async def vopros_ryss(message: Message):
    await message.answer('Открываю меню: Подготовка к зачету по русскому языку', reply_markup=kb.vopros_ryss)


@dp.message(F.text.lower() == 'меню вопросов по русскому языку')
async def vopros_ryss(message: Message):
    await message.answer('Открываю меню: Подготовка к зачету по русскому языку', reply_markup=kb.vopros_ryss)


@dp.message(Command('admin'))
async def admin_the_panel(message: Message):
    if message.from_user.id in (ID_ADMIN, USER_Anastasia_Borodina):
        await message.answer('Добро пожаловать в админ панель', reply_markup=kb.admin_panel)
    else:
        await message.answer('У вас недостаточно прав')


@dp.message(F.text.lower() == 'отправить сообщение')
async def admin_panel(message: Message):
    await message.answer("Выберите получателя", reply_markup=kb.user_sms)


@dp.message(F.text.lower() == 'написать всем пользователям')
async def reg_help(message: Message, state: FSMContext):
    if message.from_user.id == ID_ADMIN:
        await state.set_state(Reg.sms_user_all)
        await message.answer('Введите текст который будет отправлен всем пользователям бота', reply_markup=kb.other)
    else:
        await message.answer('Эта функция доступна только для администрации бота')


@dp.message(Reg.sms_user_all)
async def reg_help_test(message: Message, state: FSMContext):
    await state.update_data(sms_user_all=message.text)
    data = await state.get_data()
    await message.answer('Сообщение отправляется всем пользователям', reply_markup=kb.main)
    await bot.send_message(ID_ADMIN, f'{data["sms_user_all"]}')
    await bot.send_message(ID_USER_Maria_Malashta, f'{data["sms_user_all"]}')
    await bot.send_message(ID_USER_Sofi_Leuhina, f'{data["sms_user_all"]}')
    await bot.send_message(USER_NasimLat, f'{data["sms_user_all"]}')
    await bot.send_message(USER_3, f'{data["sms_user_all"]}')
    await bot.send_message(USER_4, f'{data["sms_user_all"]}')
    await state.clear()


@dp.message(F.text.lower() == 'написать maria_malashta')
async def reg_help(message: Message, state: FSMContext):
    if message.from_user.id == ID_ADMIN:
        await state.set_state(Reg.sms_user_Maria_Malashta)
        await message.answer('Введите текст который будет отправлен всем пользователям бота', reply_markup=kb.other)
    else:
        await message.answer('Эта функция доступна только для администрации бота')


@dp.message(Reg.sms_user_Maria_Malashta)
async def reg_help_test(message: Message, state: FSMContext):
    await state.update_data(sms_user_Maria_Malashta=message.text)
    data = await state.get_data()
    await message.answer('Сообщение отправляется всем пользователям', reply_markup=kb.main)
    await bot.send_message(ID_USER_Maria_Malashta, f'{data["sms_user_Maria_Malashta"]}')
    await state.clear()


@dp.message(F.text.lower() == 'вопрос 1')
async def vopros_ryss1(message: Message):
    await message.answer(t.vopros_ryss1())
    await message.answer(t.otvet_ryss1(), reply_markup=kb.vopros1)


@dp.message(F.text.lower() == 'вопрос 2')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros2)


@dp.message(F.text.lower() == 'вопрос 3')
async def vopros_ryss3(message: Message):
    await message.answer(t.vopros_ryss3())
    await message.answer(t.otvet_ryss3(), reply_markup=kb.vopros3)


@dp.message(F.text.lower() == 'вопрос 4')
async def vopros_ryss4(message: Message):
    await message.answer(t.vopros_ryss4())
    await message.answer(t.otvet_ryss4(), reply_markup=kb.vopros4)


@dp.message(F.text.lower() == 'вопрос 5')
async def vopros_ryss4(message: Message):
    await message.answer(t.vopros_ryss5())
    await message.answer(t.otvet_ryss5(), reply_markup=kb.vopros5)


@dp.message(F.text.lower() == 'вопрос 6')
async def vopros_ryss6(message: Message):
    await message.answer(t.vopros_ryss6())
    await message.answer(t.otvet_ryss6(), reply_markup=kb.vopros6)


@dp.message(F.text.lower() == 'вопрос 7')
async def vopros_ryss7(message: Message):
    await message.answer(t.vopros_ryss7())
    await message.answer(t.otvet_ryss7(), reply_markup=kb.vopros7)


@dp.message(F.text.lower() == 'вопрос 8')
async def vopros_ryss8(message: Message):
    await message.answer(t.vopros_ryss8())
    await message.answer(t.otvet_ryss8(), reply_markup=kb.vopros8)


@dp.message(F.text.lower() == 'вопрос 9')
async def vopros_ryss9(message: Message):
    await message.answer(t.vopros_ryss9())
    await message.answer(t.otvet_ryss9(), reply_markup=kb.vopros9)


@dp.message(F.text.lower() == 'вопрос 10')
async def vopros_ryss10(message: Message):
    await message.answer(t.vopros_ryss10())
    await message.answer(t.otvet_ryss10(), reply_markup=kb.vopros10)


@dp.message(F.text.lower() == 'вопрос 11')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss11())
    await message.answer(t.otvet_ryss11(), reply_markup=kb.vopros11)


@dp.message(F.text.lower() == 'вопрос 12')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss12())
    await message.answer(t.otvet_ryss12(), reply_markup=kb.vopros12)


@dp.message(F.text.lower() == 'вопрос 13')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss13())
    await message.answer(t.otvet_ryss13(), reply_markup=kb.vopros13)


@dp.message(F.text.lower() == 'вопрос 14')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss14())
    await message.answer(t.otvet_ryss14(), reply_markup=kb.vopros14)


@dp.message(F.text.lower() == 'вопрос 15')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss15())
    await message.answer(t.otvet_ryss15(), reply_markup=kb.vopros15)


@dp.message(F.text.lower() == 'вопрос 16')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss16())
    await message.answer(t.otvet_ryss16(), reply_markup=kb.vopros16)


@dp.message(F.text.lower() == 'вопрос 17')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss17())
    await message.answer(t.otvet_ryss17(), reply_markup=kb.vopros17)


@dp.message(F.text.lower() == 'вопрос 18')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss18())
    await message.answer(t.otvet_ryss18(), reply_markup=kb.vopros18)


@dp.message(F.text.lower() == 'вопрос 19')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss19())
    await message.answer(t.otvet_ryss19(), reply_markup=kb.vopros19)


@dp.message(F.text.lower() == 'вопрос 20')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss20())
    await message.answer(t.otvet_ryss20(), reply_markup=kb.vopros20)


@dp.message(F.text.lower() == 'вопрос 21')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss21())
    await message.answer(t.otvet_ryss21(), reply_markup=kb.vopros21)


@dp.message(F.text.lower() == 'вопрос 22')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss22())
    await message.answer(t.otvet_ryss22(), reply_markup=kb.vopros22)


@dp.message(F.text.lower() == 'вопрос 23')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss23())
    await message.answer(t.otvet_ryss23(), reply_markup=kb.vopros23)


@dp.message(F.text.lower() == 'вопрос 24')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss24())
    await message.answer(t.otvet_ryss24(), reply_markup=kb.vopros24)


@dp.message(F.text.lower() == 'вопрос 25')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss25())
    await message.answer(t.otvet_ryss25(), reply_markup=kb.vopros25)


@dp.message(F.text.lower() == 'вопрос 26')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss26())
    await message.answer(t.otvet_ryss26(), reply_markup=kb.vopros26)


@dp.message(F.text.lower() == 'вопрос 27')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss27())
    await message.answer(t.otvet_ryss27(), reply_markup=kb.vopros27)


@dp.message(F.text.lower() == 'вопрос 28')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss28())
    await message.answer(t.otvet_ryss28(), reply_markup=kb.vopros28)


@dp.message(F.text.lower() == 'вопрос 29')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss29())
    await message.answer(t.otvet_ryss29(), reply_markup=kb.vopros29)


@dp.message(F.text.lower() == 'вопрос 30')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss30())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros30)


@dp.message(F.text.lower() == 'вопрос 31')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros31)


@dp.message(F.text.lower() == 'вопрос 32')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros32)


@dp.message(F.text.lower() == 'вопрос 33')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros33)


@dp.message(F.text.lower() == 'вопрос 34')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros34)


@dp.message(F.text.lower() == 'вопрос 35')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros35)


@dp.message(F.text.lower() == 'вопрос 36')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros36)


@dp.message(F.text.lower() == 'вопрос 37')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros37)


@dp.message(F.text.lower() == 'вопрос 38')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros38)


@dp.message(F.text.lower() == 'вопрос 39')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros39)


@dp.message(F.text.lower() == 'вопрос 40')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros40)


@dp.message(F.text.lower() == 'вопрос 41')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros41)


@dp.message(F.text.lower() == 'вопрос 42')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros42)


@dp.message(F.text.lower() == 'вопрос 43')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros43)


@dp.message(F.text.lower() == 'вопрос 44')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros44)


@dp.message(F.text.lower() == 'вопрос 45')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros45)


@dp.message(F.text.lower() == 'вопрос 46')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros46)


@dp.message(F.text.lower() == 'вопрос 47')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros47)


@dp.message(F.text.lower() == 'вопрос 48')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros48)


@dp.message(F.text.lower() == 'вопрос 49')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros49)


@dp.message(F.text.lower() == 'вопрос 50')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros50)


@dp.message(F.text.lower() == 'вопрос 51')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros51)


@dp.message(F.text.lower() == 'вопрос 52')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros52)


@dp.message(F.text.lower() == 'вопрос 53')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros53)


@dp.message(F.text.lower() == 'вопрос 54')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros54)


@dp.message(F.text.lower() == 'вопрос 55')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros55)


@dp.message(F.text.lower() == 'вопрос 56')
async def vopros_ryss2(message: Message):
    await message.answer(t.vopros_ryss2())
    await message.answer(t.otvet_ryss2(), reply_markup=kb.vopros56)


@dp.message(F.text.lower() == 'случайные 3 вопроса')
async def vopros_ryss2(message: Message):
    await message.answer('эта кнопка на этапе разработки')


# 1410371678 админ, 1266838290 Анастасия, 5524583261 Соня
@dp.message(F.text.lower() == 'назад')
async def schedule(message: Message):
    if message.from_user.id in USER_ALL:
        await message.answer("Открываю главное меню",
                             reply_markup=kb.user_plys)
    else:
        await message.answer("Открываю главное меню",
                             reply_markup=kb.main)


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
                               caption='Нам очень жаль, что вы столкнулись с ошибкой в боте,'
                                       ' просим вас сообщить о поблеме в личном сообщении нашему администратору',
                               reply_markup=kb.help_admin)


@dp.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Рады что вы решили зарегистрироватся в нашем боте!')
    await message.answer('Введите Ваше имя\nНапример: Иван')


@dp.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона\nВ формате +7XXXXXXXXXX')


@dp.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершина.\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await bot.send_message(ID_ADMIN, (f'Регистрация пользователя ' 
                                      f'{message.from_user.first_name} {message.from_user.last_name} ' 
                                      f'завершина.\nИмя: {data["name"]}\nНомер: {data["number"]}\nID: '
                                      f'{message.from_user.id}'))
    await state.clear()


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
