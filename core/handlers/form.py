from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import States

async def get_form(message: Message, state: FSMContext):
    await message.answer('Начинаем создание поста... Введите заголовок!')
    await state.set_state(States.GET_POSTNAME)


async def get_postname(message: Message, state: FSMContext):
    await message.answer('Теперь введи текст поста.')
    await state.update_data(name=message.text)
    await state.set_state(States.GET_TEXT)

async def get_text(message: Message, state: FSMContext):
    await message.answer('Теперь отправь фотографию!')
    await state.update_data(text=message.text)
    await state.set_state(States.GET_PHOTO)

async def get_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    context_data = await state.get_data()
    post_name = context_data.get('name')
    post_text = context_data.get('text')
    post_photo = context_data.get('photo')
    await message.answer(f"Твой пост с заголовком <<{str.upper(post_name)}>> будет выглядеть так:")
    # await message.answer_photo(post_photo, caption=post_text)

    await state.clear()