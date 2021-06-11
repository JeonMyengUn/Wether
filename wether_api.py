from typing import Dict
import requests
import json


lang = "kr"
city = "Seoul"
api_key = "292c750c6a909527303e4e4465bb7a71"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric"

result = requests.get(api)

data = json.loads(result.text)

print(data['name'] + "의 날씨입니다.")
print("날씨는", data['weather'][0]['description'], "입니다.")
print("현재 온도는", data['main']['temp'],"입니다.")
print("하지만 체감 온도는", data['main']['feels_like'],"입니다.")
print("최저기온은", data['main']['temp_min'], "이고,")
print("최고기온은", data['main']['temp_max'],"입니다.")
print("습도 : ", data['main']['humidity'])
print("기압 : ", data['main']['pressure'])
print("풍향 : ", data['wind']['deg'])
print("풍속 : ", data['wind']['speed'], "입니다.")