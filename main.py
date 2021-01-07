import requests
from pprint import pprint

def get_average(results):
    sum = 0
    count = 0
    for result in results:
        intelligence = int(result["powerstats"]["intelligence"])
        sum += intelligence
        count += 1
    return sum/count

def get_average_intelligence_from_api(name):
    response = requests.get("https://www.superheroapi.com/api.php/2619421814940190/search/{}".format(name))
    response.raise_for_status()
    results = response.json()["results"]
    return get_average(results)


def get_most_intelligent_superhero(names):
    max_intelligence = 0
    max_name = None
    for name in names:
        intelligence = get_average_intelligence_from_api(name)
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            max_name = name
    return max_name

print(get_most_intelligent_superhero(["Hulk", "Thanos", "Captain America"]))


