import requests
from elasticsearch import Elasticsearch
def odessa_api():
    es = Elasticsearch()

    token = 'af6aee6f630193da703b367300aca057'

    response = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=odessa,ua&&units=metric&appid='+token)

    data = response.json()
    temp = []

    for number in range(8):
        temp.append(data['list'][number]['main']['temp'])
    firstDayMax = max(temp)
    firstDayMin = min(temp)

    temp.clear()
    for number in range(9, 16):
        temp.append(data['list'][number]['main']['temp'])
    secondDayMax = max(temp)
    secondDayMin = min(temp)

    temp.clear()
    for number in range(17, 24):
        temp.append(data['list'][number]['main']['temp'])
    thirdDayMax = max(temp)
    thirdDayMin = min(temp)

    odessaWeather = {
        'firstMin': round(firstDayMin),
        'firstMax': round(firstDayMax),
        'secondMin': round(secondDayMin),
        'secondMax': round(secondDayMax),
        'thirdMin': round(thirdDayMin),
        'thirdMax': round(thirdDayMax),
    }
    res = es.index(index="odessaapi", id=4, body=odessaWeather)
    print(res['result'])






