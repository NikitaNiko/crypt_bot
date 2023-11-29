from aiogram import Dispatcher, Bot
import asyncio
from senders import sending
from user_mes import user_messages, user_commands, coin_states


bot1 = Bot("5647971616:AAEUmfKipJ7t2rk-tbIHcYHGfZWNTyg5WaM")

async def main():
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        user_messages.router,
        coin_states.router,
    )
    await bot1.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot1)

if __name__ == "__main__":
    asyncio.run(main())
    