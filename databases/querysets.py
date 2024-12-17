from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from databases.models import *

# async def add_genre():
#     async with async_session() as session:
#         genre = Genre(
#             name="Fantasy", 
#             description="The fantasy genre features magical and supernatural elements, mythical creatures, and imaginative worlds, often exploring the battle between good and evil."
#         )
#         session.add(genre)
#         await session.commit()


# async def add_url():
#     async with async_session() as session:
#         url = Url(
#             url="https://www.imdb.com/title/tt1170358/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_the%2520hobb"
#         )
#         session.add(url)
#         await session.commit()


# async def add_actors():
#     async with async_session() as session:
#         actor = Actors(
#             image='images/emilia_clarke.png', 
#             first_name='Emilia', 
#             last_name="Clarke", 
#             birth_day='1986-10-23', 
#             description="Emilia Clarke is an English actress best known for her role as Daenerys Targaryen in Game of Thrones. She has received multiple award nominations and is an advocate for global health initiatives."
#         )
#         session.add(actor)
#         await session.commit()


# async def add_director():
#     async with async_session() as session:
#         director = Directors(
#             image="images/peter_jackson.png", 
#             first_name="Peter", 
#             last_name="Jackson", 
#             birth_day="1961-10-31", 
#             description="Peter Jackson is a New Zealand filmmaker and screenwriter best known for directing The Lord of the Rings and The Hobbit trilogies. His epic adaptations have redefined modern fantasy cinema."
#         )
#         session.add(director)
#         await session.commit()


# async def add_movie():
#     async with async_session() as session:
#         movie = Movies(
#             poster="images/the_hobbit.png", 
#             title="The Hobbit: An Unexpected Journey", 
#             release_date="2012-12-14", 
#             description="A reluctant hobbit, Bilbo Baggins, sets out on a quest to help dwarves reclaim their homeland from the dragon Smaug, encountering adventure and peril along the way.", 
#             country="New Zealand/USA", 
#             age_limit=12, 
#             trailer="trailers/the_hobbit.png",
#             url_id = 6
#         )
#         session.add(movie)
#         await session.commit()


# async def add_series():
#     async with async_session() as session:
#         series = Series(
#             poster="images/game_of_trones.png", 
#             title="Game of trones", 
#             release_date="2011-04-17", 
#             description="In the mythical land of Westeros, noble families vie for control of the Iron Throne, facing treachery, betrayal, and an ancient enemy that threatens them all.", 
#             country="USA", 
#             age_limit=18, 
#             trailer="trailers/game_of_trones.png",
#             seasons = 8,
#             url_id = 5
#         )
#         session.add(series)
#         await session.commit()

# async def add_actor_to_movie():
#     async with async_session() as session:
#         stmt = movie_actors.insert().values(movie_id=3, actor_id=5)
#         await session.execute(stmt)
#         await session.commit()

# async def add_movie_genres():
#     async with async_session() as session:
#         stmt = movie_genre.insert().values(movie_id=3, genre_id=4)
#         await session.execute(stmt)
#         await session.commit()
        
# async def add_movie_directors():
#     async with async_session() as session:
#         stmt = movie_directors.insert().values(movie_id=2, director_id=1)
#         await session.execute(stmt)
#         await session.commit()

# async def add_actor_to_series():
#     async with async_session() as session:
#         stmt = series_actors.insert().values(series_id=3, actor_id=1)
#         await session.execute(stmt)
#         await session.commit()

# async def add_series_genres():
#     async with async_session() as session:
#         stmt = series_genre.insert().values(series_id=1, genre_id=3)
#         await session.execute(stmt)
#         await session.commit()
        
# async def add_series_directors():
#     async with async_session() as session:
#         stmt = series_directors.insert().values(series_id=2, director_id=1)
#         await session.execute(stmt)
#         await session.commit()
    

async def all_movies():
    async with async_session() as session:
        result = await session.scalars(select(Movies))
        return result

async def all_series():
    async with async_session() as session:
        result = await session.scalars(select(Series))
        return result

async def all_genre():
    async with async_session() as session:
        result = await session.scalars(select(Genre))
        return result
    
async def all_actors():
    async with async_session() as session:
        result = await session.scalars(select(Actors))
        return result

async def all_directors():
    async with async_session() as session:
        result = await session.scalars(select(Directors)) 
        return result


async def get_movie_by_id(movie_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Movies).where(Movies.id == movie_id))
        return result

async def get_series_by_id(series_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Series).where(Series.id == series_id))
        return result

async def get_movie_by_genre(genre_id: int):
    async with async_session() as session:
        result = await session.scalars(
            select(Movies).join(movie_genre).where(movie_genre.c.genre_id == genre_id)
        )
        return result

async def get_movie_by_actor(actor_id):
    async with async_session() as session:
        result = await session.scalars(
            select(Movies).join(movie_actors).where(movie_actors.c.actor_id == actor_id) 
        )
        return result

async def get_movie_by_director(director_id):
    async with async_session() as session:
        result = await session.scalars(
            select(Movies).join(movie_directors).where(movie_directors.c.director_id == director_id) 
        )
        return result