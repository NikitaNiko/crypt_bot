import requests, asyncio
from bs4 import BeautifulSoup as BS

sites = [
        "https://coinmarketcap.com/currencies/atletico-de-madrid-fan-token/",
        "https://coinmarketcap.com/currencies/powerpool/",
        "https://coinmarketcap.com/currencies/lido-dao/",
        "https://coinmarketcap.com/currencies/1inch/",
        "https://coinmarketcap.com/currencies/near-protocol/",
        "https://coinmarketcap.com/currencies/gas/"
    ]

async def getting():

    answers = {}
    num = 1
    ret = ""

    for site in range(len(sites)):
        answers.update({site+1: None})

    sess = requests.Session()

    for site in sites:
        r = sess.get(site)
        html = BS(r.content, 'html.parser')

        for el in html.select(".hgNnJe"):
            name = el.select(".gYiXVQ")
            price = el.select(".flfGQp > span")
            percent  = el.select(".flfGQp > .cOoglq")
            # print(f"({name[0].text}) цена сейчас: " + price[0].text)
            # print(percent[0].text)
        
        answers[num] = name[0].text, price[0].text, percent[0].text
        num += 1
    
    for key in answers.keys():
        ret += f"😎{answers[key][0]} \n🤑Цена: {answers[key][1]} \n🤔Изменение в процентах: {answers[key][2]}\n\n"

    return ret


async def price(list_sites):

    ses = requests.Session()
    asnwers = []

    for site in list_sites:
        r = ses.get(site)
        html = BS(r.content, 'html.parser')

        for el in html.select(".hgNnJe"):
            name = el.select(".gYiXVQ")
            price = el.select(".flfGQp > span")
            asnwers.append(f"{name[0].text}: {price[0].text[1:]}")

    return asnwers

