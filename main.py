from handlers.user_handlers import register

import asyncio
# aiogram
from aiogram import Dispatcher, Bot


async def main():
    bot = Bot(token='TOKEN')
    dp = Dispatcher()
    register(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
