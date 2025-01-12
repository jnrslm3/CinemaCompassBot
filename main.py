import asyncio
from aiogram import Bot, Dispatcher
from databases.models import *
import sys, logging
from config import TOKEN
from commands.command import command_router
from databases.models import create_tables
from databases.querysets import *

async def main():
    # await create_tables()
    # await add_actor_to_movie()
    # await add_movie_genres()
    # await add_movie_directors()
    # await add_actor_to_series()
    # await add_series_genres()
    # await add_series_directors()
    # await add_genre()
    # await add_url()
    # await add_actors()
    # await add_director()
    # await add_movie()
    # await add_series()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(command_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())














