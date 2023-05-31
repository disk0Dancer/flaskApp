from userApp import userApp
import random, string


# Интерфейс для передачи ссылок на функции для PUG файлов
@userApp.context_processor
def example():
    return dict(randomString=randomString)

# Функция для предотвращения кеширования JS браузером
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
