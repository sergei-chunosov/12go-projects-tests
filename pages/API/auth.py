import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')


class Auth:

    def get_cookie(self, user_name=user_name, password=password):
        session = requests.Session()
        jsonAuth = json.dumps({"email": user_name, "password": password}, ensure_ascii=False).encode('utf8')
        url = 'https://12go.asia/api/nuxt/en/user/auth'
        session.post(url, jsonAuth)
        cookies = session.cookies.get('autht4')
        return cookies


auth = Auth()