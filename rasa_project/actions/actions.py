import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"
    
    def run(self, dispatcher, tracker, domain):
        base_url = "http://api.weatherapi.com/v1/current.json"
        api_key = "token"
        city = "Moscow"
        complete_url = f"{base_url}?key={api_key}&q={city}&aqi=no"
        response = requests.get(complete_url)
        data = response.json()
        temp = data["current"]["temp_c"]
        #dispatcher.utter_message(text=f"Сейчас {temp}")
        print(data)
        return [
            SlotSet("temp", temp)
        ]