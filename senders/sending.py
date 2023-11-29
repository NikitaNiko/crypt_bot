from bot import bot1
from threading import Thread
from aiogram import types
import asyncio, math
from requests_bot import bitcoin

sites = [
        "https://coinmarketcap.com/currencies/atletico-de-madrid-fan-token/",
        "https://coinmarketcap.com/currencies/powerpool/",
        "https://coinmarketcap.com/currencies/lido-dao/",
        "https://coinmarketcap.com/currencies/1inch/",
        "https://coinmarketcap.com/currencies/near-protocol/",
        "https://coinmarketcap.com/currencies/gas/",
    ]

async def test():

    ans = await bitcoin.price(sites)

    while True:

        await asyncio.sleep(30)
        new = await bitcoin.price(bitcoin.sites)
        changes = ""

        print(new)

        for i in range(len(new)):
            # Выборка стоимости из всей строки в str!!!
            old_price = float(ans[i][ans[i].find(":") + 1:])
            new_price = float(new[i][new[i].find(":") + 1:])
            
            if (ans[i] != new[i] and abs(old_price - new_price) > 0.05):
                if (old_price > new_price):
                    changes += f"\n👀{ans[i]} ->\n☠{new[i]}\n"
                else:
                    changes += f"\n👀{ans[i]} ->\n📈{new[i]}\n"

        if (changes != ""):
            ans = new
            await bot1.send_message(234706554, "♻Изменения курса:\n" + changes)
            # await bot1.send_message(6497684959, "♻Изменения курса:\n" + changes)
            
def go():
    asyncio.run(test())


t1 = Thread(target=go)

t1.start()

