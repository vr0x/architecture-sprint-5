from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ActionExecuted, FollowupAction

class ActionProvideTechInfo(Action):
    def name(self):
        return "action_provide_some_tech_info"

    def run(self, dispatcher, tracker, domain):
            tech = tracker.get_slot("some_tech")

            tech_info = {
                "Kafka": "Kafka — Это инструмент для обеспечения взаимодействия между микросервисами. Посредник для передачи сообщений между микросервисами",
                "Docker": "Docker — это платформа для контейнеризации приложений.",
                "Kubernetes": "Kubernetes — это система для управления контейнеризированными приложениями."
            }

            response = tech_info.get(tech, f"Извините, у меня нет информации о {tech}.")

            dispatcher.utter_message(response)
            return [
              SlotSet('related_tech', tech),
              FollowupAction("action_provide_async_patterns")
            ]
            return []

class ActionProvideAsyncPatterns(Action):
    def name(self):
        return "action_provide_async_patterns"

    def run(self, dispatcher, tracker, domain):
        pattern = tracker.get_slot("related_tech")
        tech_patterns = {
            "Kafka": "В основе Kafka заложен паттерн асинхронного взаимодействия: Message Queueing этот паттерн представляет собой очередь событий. Из которой подписчики могут брать события в обработку",
        }
        response = tech_patterns.get(pattern)
        if response:
          dispatcher.utter_message(response)
        return []