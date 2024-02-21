#This code will take the weather in the location and let you know if it is going to rain and if it will rain int h enxt hour or so then it will text and let you know to bring an umbrella


from requests import *
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "d6419091ee506b0d84f3ec1f10ad55ec"
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACf003ae70df060b5552330f1a04fd2ae9'
auth_token = 'c1d5599b3ec6b817bd7e7f09e641be4e'


wparams = {
    "lat":33.696369,
    "lon": -84.291542,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

one_call = get(OWM_Endpoint, params= wparams)
one_call.raise_for_status()
data = one_call.json()

#Drilling down the JSON dictionary and list to get to the weather ID
# hourly = data["hourly"][0]["weather"][0]["id"]

hourly_slice = data["hourly"][:12]

will_rain = False

for hour in hourly_slice:
    ids = hour["weather"][0]["id"]
    if int(ids) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella",
        from_='+12173354708',
        to='+1 678 357 8436'
        )

print(message.status)

