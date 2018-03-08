import requests

id = "84600bca7507293656495e8972aec659"
payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':id}

def query_weather(payload):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(endpoint, params=payload)

    return response

response = query_weather(payload)