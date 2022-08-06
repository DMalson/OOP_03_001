import requests

def getjson(url):
    resp = requests.get(url)
    return(resp.json())

def findsmartest(list_of_all, heroes_list):
    smartest_hero = ''
    hero_intelligence = 0
    for item in list_of_all:
        if item['name'] in heroes_list:
            print(f"{item['name']} - {item['powerstats']['intelligence']}")
            if int(item['powerstats']['intelligence']) > hero_intelligence:
                hero_intelligence = int(item['powerstats']['intelligence'])
                smartest_hero = item['name']
    return [smartest_hero, str(hero_intelligence)]

if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resplist = getjson(url)
    print(f"Smartest hero is {' - '.join(findsmartest(resplist,['Hulk', 'Captain America', 'Thanos']))} intelligence")
