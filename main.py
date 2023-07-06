from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import *
from core.settings import settings
from aiogram.filters import Text, Command 
from core.utils.commands import set_commands

import asyncio
import logging

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot is running')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    
    dp.startup.register(start_bot)
    
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_start, Command(commands=['new_post']))
    dp.message.register(get_start, Text('Создать новый пост'))

    dp.message.register(descr_command, Command(commands='description'))
    

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())