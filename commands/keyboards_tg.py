from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databases.querysets import *

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог фильмов')],
        [KeyboardButton(text='Каталог сериалов')],
        [KeyboardButton(text='Каталог жанров')],
        [KeyboardButton(text='Поиск по актерам')],
        [KeyboardButton(text='Поиск по режиссерам')],
        [KeyboardButton(text='Поиск фильма по названию')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите кнопку'
)

async def get_movies_kb():
    kb = InlineKeyboardBuilder()
    movies = await all_movies()
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title, callback_data=f"movie_{movie.id}"))
    return kb.adjust(2).as_markup()

async def get_series_kb():
    kb = InlineKeyboardBuilder()
    series = await all_series()
    for seria in series:
        kb.add(InlineKeyboardButton(text=seria.title, callback_data=f"seria_{seria.id}"))
    return kb.adjust(2).as_markup()

async def get_genre_kb():
    kb = InlineKeyboardBuilder()
    genres = await all_genre()
    for genre in genres:
        kb.add(InlineKeyboardButton(text=genre.name, callback_data=f"genre_{genre.id}"))
    return kb.adjust(2).as_markup()

async def get_actors_kb():
    kb = InlineKeyboardBuilder()
    actors = await all_actors()
    for actor in actors:
        kb.add(InlineKeyboardButton(text=f"{actor.first_name} {actor.last_name}", callback_data=f"actor_{actor.id}"))
    return kb.adjust(2).as_markup()

async def get_directors_kb():
    kb = InlineKeyboardBuilder()
    directors = await all_directors()
    for director in directors:
        kb.add(InlineKeyboardButton(text=f"{director.first_name} {director.last_name}", callback_data=f"director_{director.id}"))
    return kb.adjust(2).as_markup()


async def get_movies_by_genre_kb(genre_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_genre(genre_id)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title, callback_data=f"movie_{movie.id}"))
    return kb.adjust(2).as_markup()

async def get_actores_kb():
    kb = InlineKeyboardBuilder()
    actores = await all_actors() 
    for actors in actores: 
        kb.add(InlineKeyboardButton(text=f"{actors.first_name} {actors.last_name}", 
            callback_data=f"actor_{actors.id}"))    
    return kb.adjust(2).as_markup()

async def get_movies_by_actors_kb(actor_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_actor(actor_id)  
    for movie in movies: 
        kb.add(InlineKeyboardButton(text=movie.title, 
            callback_data=f"movie_{movie.id}"))    
    return kb.adjust(2).as_markup() 

async def get_directores_kb():
    kb = InlineKeyboardBuilder()
    directores = await all_directors() 
    for directors in directores: 
        kb.add(InlineKeyboardButton(text=f"{directors.first_name} {directors.last_name}", 
            callback_data=f"director_{directors.id}"))   
    return kb.adjust(2).as_markup()


async def get_movies_by_directors_kb(director_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_director(director_id)  
    for movie in movies: 
        kb.add(InlineKeyboardButton(text=movie.title, 
            callback_data=f"movie_{movie.id}"))    
    return kb.adjust(2).as_markup() 

