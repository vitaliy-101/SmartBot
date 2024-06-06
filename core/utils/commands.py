from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало работы"),
        BotCommand(command="help", description="Помошь"),
        BotCommand(command="donation", description="Пожертвование"),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
