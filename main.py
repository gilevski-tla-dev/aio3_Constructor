from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
from core.settings import settings
from aiogram.filters import Text, Command 

import asyncio
import logging

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot is running')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_start, Text('Создать новый пост'))

    dp.startup.register(start_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())