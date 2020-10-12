import sys
import os
import requests

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("BOT_CHAT")

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
text = f"Build {sys.argv[1]}"

requests.get(url, data={'chat_id': chat_id, 'text': text})
