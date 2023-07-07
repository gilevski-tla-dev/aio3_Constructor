from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Приветствую Вас, <b>{message.from_user.first_name}</b>.\n\nБлагодаря этому боту вы можете создать посты на своем сайте.\n\nНажмите на кнопку <b>меню</b>, чтобы увидеть список команд.')


async def descr_command(message: Message, bot: Bot):
    await message.answer('Благодаря этому боту вы можете размещать на сайте посты, фотографии, менять темы и оформление.') 

   