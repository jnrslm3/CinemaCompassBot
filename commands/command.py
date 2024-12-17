from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import F
from commands.keyboards_tg import *
from aiogram.utils.media_group import MediaGroupBuilder
from databases.querysets import *

command_router = Router()

@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        f"Привет, @{message.from_user.username}, я бот по подборке фильмов и сериалов.",
        reply_markup=kb
    )

@command_router.message(F.text == 'Каталог фильмов')
async def movies_handler(message: Message):
    await message.answer("Каталог фильмов", reply_markup=await get_movies_kb())

@command_router.message(F.text == 'Каталог сериалов')
async def series_handler(message: Message):
    await message.answer('Каталог сериалов', reply_markup=await get_series_kb())

@command_router.message(F.text == 'Каталог жанров')
async def genre_handler(message: Message):
    await message.answer('Каталог жанров', reply_markup=await get_genre_kb())

@command_router.message(F.text == 'Поиск по актерам')
async def actors_handler(message: Message):
    await message.answer('Поиск по актерам', reply_markup=await get_actors_kb())

@command_router.message(F.text == 'Поиск по режиссерам')
async def directors_handler(message: Message):
    await message.answer('Поиск по режиссерам', reply_markup=await get_directors_kb())

@command_router.callback_query(F.data.startswith('movie_'))
async def movie_details_handler(callback: CallbackQuery):
    movie_id = int(callback.data.split('_')[1])  
    movie = await get_movie_by_id(movie_id=movie_id)
    
    if not movie:
        await callback.message.answer("Фильм не найден.")
        return
    
    album = MediaGroupBuilder()
    description = (
        f'Название: {movie.title}\n'
        f'Год выпуска: {movie.release_date}\n'
        f'Описание: {movie.description}\n'
        f'Страна: {movie.country}\n'
        f'Возрастное ограничение: {movie.age_limit}\n'
    )
    
    if movie.poster.startswith('http') or movie.poster.startswith("AgA"):
        album.add_photo(media=movie.poster, caption=description)
    else:
        album.add_photo(media=FSInputFile(movie.poster), caption=description)

    if movie.trailer.startswith('http') or movie.trailer.startswith("AgA"):
        album.add_video(media=movie.trailer)
    else:
        album.add_video(media=FSInputFile(movie.trailer))
    
    await callback.message.answer_media_group(media=album.build())



@command_router.callback_query(F.data.startswith('seria_'))
async def series_details_handler(callback: CallbackQuery):
    series_id = int(callback.data.split('_')[1])  
    series = await get_series_by_id(series_id = series_id)
    
    if not series:
        await callback.message.answer("Сериал не найден.")
        return
    
    album = MediaGroupBuilder()
    description = (
        f'Название: {series.title}\n'
        f'Год выпуска: {series.release_date}\n'
        f'Описание: {series.description}\n'
        f'Страна: {series.country}\n'
        f'Возрастное ограничение: {series.age_limit}\n'
        f'Сезоны: {series.seasons}\n'
    )
    
    if series.poster.startswith('http') or series.poster.startswith("AgA"):
        album.add_photo(media=series.poster, caption=description)
    else:
        album.add_photo(media=FSInputFile(series.poster), caption=description)

    if series.trailer.startswith('http') or series.trailer.startswith("AgA"):
        album.add_video(media=series.trailer)
    else:
        album.add_video(media=FSInputFile(series.trailer))
    
    await callback.message.answer_media_group(media=album.build())


@command_router.callback_query(F.data.startswith('genre_'))
async def movie_by_genre_handler(callback: CallbackQuery):
    g_id = callback.data.split('_')[1]  # genre_1
    await callback.message.answer(f'Фильмы по жанру',
         reply_markup=await get_movies_by_genre_kb(g_id))



@command_router.callback_query(F.data.startswith('actor_'))
async def movie_by_actors_handler(callback: CallbackQuery):
    a_id = callback.data.split('_')[1] 
    await callback.message.answer(f"Фильмы с этим актёром:",
        reply_markup=await get_movies_by_actors_kb(a_id))


@command_router.callback_query(F.data.startswith('director_'))
async def movie_by_directors_handler(callback: CallbackQuery):
    d_id = callback.data.split('_')[1] 
    await callback.message.answer(f"Фильмы у этого режиссёра:",
        reply_markup=await get_movies_by_directors_kb(d_id)) 
