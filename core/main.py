import asyncio
from aiogram import Bot, Dispatcher
from core.Settings import settings
from core.utils.commands import set_commands
from handlers import donation
import logging


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(settings.bots.bot_token)
    bot.default.parse_mode = 'HTML'
    dp = Dispatcher()
    dp.include_router(donation.router)

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
