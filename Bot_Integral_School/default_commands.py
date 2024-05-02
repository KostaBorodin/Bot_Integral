from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


# todo Дописать свои команды в меню команд
async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="start", description="Запуск бота 🏁"),
        BotCommand(command="help", description="Список команд 🗂"),
        BotCommand(command="hadm", description="Связь с администратором 👨‍💻"),
        BotCommand(command="reg", description="Зарегистрироваться в Botintegral"),
        BotCommand(command="ry8b", description="Расписание уроков 8Б 🗓"),
        BotCommand(command="admin", description="Админ панель (доступна только для администрации)"),

    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )
