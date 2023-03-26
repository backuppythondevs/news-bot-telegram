import os
from dotenv import load_dotenv


# leer el archivo .env
load_dotenv()

TOKEN_API_TELEGRAM = os.getenv('TELEGRAM_TOKEN_API')
API_NEW_TOKEN = os.getenv('API_NEW_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')