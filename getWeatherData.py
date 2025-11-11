import requests
city = "Pesahwar"
api_key = "API_KEY_HERE"
url = f"https://api.openweathermap.org/data/2.5/weather?q={Peshawar}&appid={api_key}"
print(requests.get(url).json)