from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ActionExecuted, FollowupAction

class ActionProvideTechInfo(Action):
    def name(self):
        return "action_provide_some_tech_info"

    def run(self, dispatcher, tracker, domain):
            tech = tracker.get_slot("some_tech")

            def find_tech_in_list(arr, target):
                for element in arr:
                    if element == target:
                        return element  # Возвращаем найденный элемент
                return False

            brokers = ["kafka", "rabbitmq"]

            broker = find_tech_in_list(brokers, tech.lower())
            if broker:
              return [
                SlotSet('related_tech', tech),
                FollowupAction("action_provide_brokers")
              ]
            return []

class ActionProvideBrokersTechInfo(Action):
  def name(self):
    return "action_provide_brokers"

  def run(self, dispatcher, tracker, domain):
      broker = tracker.get_slot("related_tech")
      tech_brokers = {
          "kafka": """
            <p>Apache Kafka – это распределенная платформа потоковой передачи событий с открытым исходным кодом, обеспечивающая высокую пропускную способность. Написанная на Java и Scala, Кафка представляет собой шину сообщений системы Pub/Sub, ориентированную на потоки и воспроизведение данных с высокой интенсивностью.</p>
            <p>Кафка не полагается на очередь, а добавляет сообщения в журнал и оставляет их там до достижения предела хранения или тех пор, пока консьюмер не прочитает эти сообщения</p>
            <p>Apache Kafka использует неограниченный поток данных, при этом пары «ключ-значение» непрерывно передаются в назначенную тему.</p>
            """,
          "rabbitMQ": """
            <p><strong>RabbitMQ</strong> – распределённый и горизонтально масштабируемый брокер сообщений</p>
            <p>Основное преимущество RabbitMQ — гибкая маршрутизация. Сообщения маршрутизируются через exchange (обменник) перед попаданием в очереди. RabbitMQ предлагает несколько встроенных типов обмена для типичной логики маршрутизации</p>
            <p>RabbitMQ использует модель умный брокер/тупой консьюмер. Брокер последовательно доставляет сообщения консьюмерам и отслеживает их статус.</p>
          """
      }
      response = tech_brokers.get(broker.lower())
      if response:
        dispatcher.utter_message(response)

      return []

class ActionProvideAsyncPatterns(Action):
    def name(self):
        return "action_provide_async_patterns"

    def run(self, dispatcher, tracker, domain):
        pattern = tracker.get_slot("interaction_pattern")
        tech_patterns = {
            "Message Queueing": "Message Queueing это паттерн проектирования для асинхронного взаимодействия. Он представляет собой очередь событий. Из которой подписчики могут брать события в обработку",
            "Pub/Sub": "Паттерн Pub/Sub (Публикация/Подписка) это паттерн проектирования для асинхронного взаимодействия. Принцип работы паттерна: есть издатель событий, есть подписчики. Когда событие происходит - подписчики получают уведомления с данными, на которые реагируют",
            "Event Sourcing": "Event Sourcing - это представитель семейства паттернов проектирования для асинхронного взаимодействия. В центре работы которого, находится не событие, а локальное состояние. При этом состояние хранится в системе не как одно значение, а как последовательность событий. Интегрировав события можно получить итоговое состояние",
            "Choreography": "Choreography - это паттерн проектирования для асинхронного взаимодействия. Принцип работы: каждый получатель события одновременно эмиттер события. Получив событие получатель генерит другое. Здесь нет централизованного управления.",
            "Orchestration": "Orchestration - это паттерн проектирования для асинхронного взаимодействия. Паттерн реализует централизованное управление событиями. Оркестратор события получает, а зачем далее определяет кому событие отправить, в зависимости от описанной у него последовательности действий"
        }
        response = tech_patterns.get(pattern)
        if response:
          dispatcher.utter_message(response)
        return []

class ActionProvideServiceBoundariesInfo(Action):
    def name(self):
        return "action_provide_service_boundaries"

    def run(self, dispatcher, tracker, domain):
        response = """
          <p>При определении границ микросервисов существуют следующие подходы:</p>
          <ul>
             <li>Функциональная декомпозиция;</li>
             <li>Принцип единой ответственности (SRP);</li>
             <li>Проектирование, ориентированное на домен (DDD);</li>
          </ul>
        """
        return []