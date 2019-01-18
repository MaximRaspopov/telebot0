import requests

class weatherBot:
    def __init__(self):
        self.proxie = "socks5://181.214.112.2:65234"
        self.appid = 'a3eacade41c258cde7fd135597d4a614'


    def weather_id(self, nameCity):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': nameCity + ',RU', 'type': 'like', 'units': 'metric', 'APPID': self.appid},
                               proxies = {"socks5" : self.proxie})
            data = res.json()
            cities = ["{} ({})".format(d['name'], d['sys']['country'])
                      for d in data['list']]
            print("city:", cities)
            city_id = data['list'][0]['id']
            return city_id
        except Exception as e:
            return None

    def weather_for_5(self, cityId):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': cityId, 'units': 'metric', 'lang': 'ru', 'APPID': self.appid},
                               proxies = {"socks5" : self.proxie})
            data = res.json()
            result = ''
            temp = ''
            for i in data['list']:
                listDt = i['dt_txt'].split(' ')
                if temp == listDt[0]:
                    result += listDt[1]+ ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ ' ' + i['weather'][0]['description'] + '\n'
                else:
                    result += '\n'
                    result += listDt[0] + '\n'
                    result += listDt[1] + ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ ' ' + i['weather'][0]['description'] + '\n'
                    temp = listDt[0]
            return result
        except Exception as e:
            return None