import os

# Секретный ключ приложения
SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'

# Настройки подключения к MongoDB
MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/db'
