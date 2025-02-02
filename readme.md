# Спринт 5 
# Грязнов М.В.

# Логи в файле log.txt

## А можешь приложить скрин переписк с ботом? Просто по логам бот ответчает 4 раза одинаковым сообщением на разный ввод
Так бот и отвечает криво.
Обучение происходит  некорректно. Валидация подготовленных данных говорит что они составленны некорректно.
Добиться вменяемого ответа у меня с ходу не получилось. 
Ниже Результат в Shell, Тест модели и результат проверки данных

### Результат  общения в Shell
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\utils\train_utils.py:530: UserWarning: constrain_similarities is set to `False`. It is recommended to set it to `True` when using cross-entropy loss.
  rasa.shared.utils.io.raise_warning(
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: 'evaluate_every_number_of_epochs=20' is greater than 'epochs=1'. No evaluation will occur.
2025-01-16 02:09:17 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  привет
Привет! Чем могу помочь в области архитектуры программного обеспечения?
Your input ->  Что такое микросервисная архитектура?
Your input ->  Неверно
Привет! Чем могу помочь в области архитектуры программного обеспечения?
Your input ->  


### Тест модели
Next message:
Привет
{
  "text": "Привет",
  "intent": {
    "name": "greet",
    "confidence": 0.22159312665462494
  },
  "entities": [],
  "text_tokens": [
    [
      0,
      6
    ]
  ],
  "intent_ranking": [
    {
      "name": "greet",
      "confidence": 0.22159312665462494
    },
    {
      "name": "request_info",
      "confidence": 0.197170227766037
    },
    {
      "name": "goodbye",
      "confidence": 0.1836010217666626
    },
    {
      "name": "affirm",
      "confidence": 0.1793060451745987
    },
    {
      "name": "deny",
      "confidence": 0.11729836463928223
    },
    {
      "name": "ask_architecture",
      "confidence": 0.10103125870227814
    }
  ],
  "response_selector": {
    "all_retrieval_intents": [],
    "default": {
      "response": {
        "responses": null,
        "confidence": 0.0,
        "intent_response_key": null,
        "utter_action": "utter_None"
      },
      "ranking": []
    }
  }
}
Next message:
Расскажите об архитектуре ПО
{
  "text": "Расскажите об архитектуре ПО",
  "intent": {
    "name": "deny",
    "confidence": 0.2703776955604553
  },
  "entities": [],
  "text_tokens": [
    [
      0,
      10
    ],
    [
      11,
      13
    ],
    [
      14,
      25
    ],
    [
      26,
      28
    ]
  ],
  "intent_ranking": [
    {
      "name": "deny",
      "confidence": 0.2703776955604553
    },
    {
      "name": "goodbye",
      "confidence": 0.2049480825662613
    },
    {
      "name": "greet",
      "confidence": 0.19518209993839264
    },
    {
      "name": "request_info",
      "confidence": 0.12545299530029297
    },
    {
      "name": "affirm",
      "confidence": 0.11444807052612305
    },
    {
      "name": "ask_architecture",
      "confidence": 0.08959101140499115
    }
  ],
  "response_selector": {
    "all_retrieval_intents": [],
    "default": {
      "response": {
        "responses": null,
        "confidence": 0.0,
        "intent_response_key": null,
        "utter_action": "utter_None"
      },
      "ranking": []
    }
  }
}
Next message:
Неверно
{
  "text": "Неверно",
  "intent": {
    "name": "greet",
    "confidence": 0.25555798411369324
  },
  "entities": [],
  "text_tokens": [
    [
      0,
      7
    ]
  ],
  "intent_ranking": [
    {
      "name": "greet",
      "confidence": 0.25555798411369324
    },
    {
      "name": "deny",
      "confidence": 0.186482235789299
    },
    {
      "name": "request_info",
      "confidence": 0.16937501728534698
    },
    {
      "name": "affirm",
      "confidence": 0.1539529263973236
    },
    {
      "name": "goodbye",
      "confidence": 0.13119877874851227
    },
    {
      "name": "ask_architecture",
      "confidence": 0.10343308001756668
    }
  ],
  "response_selector": {
    "all_retrieval_intents": [],
    "default": {
      "response": {
        "responses": null,
        "confidence": 0.0,
        "intent_response_key": null,
        "utter_action": "utter_None"
      },
      "ranking": []
    }
  }
}

### Результат rasa data validate
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The following duplicated responses have been found across multiple domain files: utter_goodbye, utter_greet
  More info at https://rasa.com/docs/rasa/domain
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: Issue found in 'data\rules.yml': 
Found intent 'ask_architecture' in stories which is not part of the domain.
  More info at https://rasa.com/docs/rasa/stories
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: Issue found in 'data\rules.yml':        
Found intent 'request_info' in stories which is not part of the domain.
  More info at https://rasa.com/docs/rasa/stories
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: Issue found in 'data\stories.yml': 
Found intent 'ask_architecture' in stories which is not part of the domain.
  More info at https://rasa.com/docs/rasa/stories
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: Issue found in 'data\stories.yml':      
Found intent 'request_info' in stories which is not part of the domain.
  More info at https://rasa.com/docs/rasa/stories
2025-01-16 02:04:56 INFO     rasa.validator  - Validating intents...
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'bot_challenge' is listed in the domain file, but is not found in the NLU training data.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'mood_great' is listed in the domain file, but is not found in the NLU training data.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'mood_unhappy' is listed in the domain file, but is not found in the NLU training data.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: There is a message in the training data labeled with intent 'request_info'. This intent is not listed in your domain. You should need to add that intent to your domain file!
  More info at https://rasa.com/docs/rasa/domain
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: There is a message in the training data labeled with intent 'ask_architecture'. This intent is not listed in your domain. You should need to add that intent to your domain file!
  More info at https://rasa.com/docs/rasa/domain
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'ask_architecture' is used in your stories, but it is not listed in the domain file. You should add it to your domain file!
  More info at https://rasa.com/docs/rasa/domain
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'request_info' is used in your stories, but it is not listed in the domain file. You should add it to your domain file!
  More info at https://rasa.com/docs/rasa/domain
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'affirm' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'bot_challenge' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'deny' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'mood_great' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The intent 'mood_unhappy' is not used in any story or rule.
2025-01-16 02:04:56 INFO     rasa.validator  - Validating uniqueness of intents and stories...
2025-01-16 02:04:56 INFO     rasa.validator  - Validating utterances...
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The utterance 'utter_happy' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The utterance 'utter_did_that_help' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The utterance 'utter_acknowledge' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The utterance 'utter_cheer_up' is not used in any story or rule.
c:\users\mike\source\repos\ya-arch-sprint-5\architecture-sprint-5\rasa_env\lib\site-packages\rasa\shared\utils\io.py:99: UserWarning: The utterance 'utter_iamabot' is not used in any story or rule.