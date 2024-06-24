#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24478892"
API_HASH = "b7b00353625f83dbf6ca2438353515a0"
BOT_TOKEN = "7409292522:AAEMTObY2Be_-ejUUo9S4p3yW5KAxKWiTBg"
SESSION = "BQEyImEAKy4yrQ_k1YOJOOY1rSzVEs_T1wfnQp7SreO7wHbJ5YxQbsqxtlZJ3ZlV5AOFqPIvZQMFU0l0_N0FRu3_jHl1-_NPhJe6tAcrcV1KQQlQc33YfYEY6o8XPkXTvlVuEmhyyMyern1_IUGN01LqxSQwEHDnXM6F6Rzs6GI4YMbuCNcy2-6BlcwohJtuJ2xZG_rbsHd4Qiy0fK5WKq7C9-ODK0XZM5t6U05uMyL13SKiP40ANDv8Q77qi-bRw6tLMfyPG5y0h0jRpreuM7UIHE-sSg3DQrKCtskltytCz3sGGps3CVUE4ntlh_s3wE0hO83wti-cbFCm2Wr0JzcxZlo1OQAAAABZEiprAA"
FORCESUB = "botsecom"
AUTH = "1494362731"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
