import json

def saver(link, coin_name):

    data = {'link': link, 'coin_name': coin_name}

    with open('data.json', 'a') as file:
        json.dump(data, file, indent=2)
        


saver("123123", "se222t")

def loader():
    
    with open('data.json', 'r') as file:
        data = json.load(file)
        for p in data:
            print(p)

loader()