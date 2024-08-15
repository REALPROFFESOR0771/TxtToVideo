import os

API_ID    = os.environ.get("API_ID", "23897874")
API_HASH  = os.environ.get("API_HASH", "ec91dd01da9693911a6ee4af5d0bef2c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7002628592:AAGEl66GunMhpKKfI9crraQLw45WZkIZxPA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
