from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Приветствую, {message.from_user.first_name}. Для того чтобы создать сайт, придумай <b>ЗАГОЛОВОК</b>')

async def descr_command(message: Message, bot: Bot):
    await message.answer('Благодаря этому боту вы можете размещать на сайте посты, фотографии, менять темы и оформление ') 

   