import requests
from twilio.rest import Client

end_point = "https://api.openweathermap.org/data/2.8/onecall"
api_key = YOUR_API"
account_sid = 'YOUR_SID'
auth_token = 'YOUR_TOKEN'

params = {
    "lat": 43.669039,
    "lon": 51.180117,
    "exclude": "daily,current,minutely,alerts",
    "appid": api_key
}
response = requests.get(url=end_point, params=params)
response.raise_for_status()
list_weather = [item for item in response.json()["hourly"] if response.json()["hourly"].index(item) < 12]
rain = False
for item in list_weather:
    if item["weather"][0]["id"] < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Take an umbrella☂",
        from_='+18642522521',
        to='YOUR_PHONE_NIMBER'
    )
    print(message.status)

