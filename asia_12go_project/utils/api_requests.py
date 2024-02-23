import requests
from allure_commons._allure import step
from dotenv import load_dotenv
import os
import json
from asia_12go_project.utils.logging_helper import logging_helper

load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')


def post_request(url, json):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, json=json)
        logging_helper(response)
    return response


def get_request(url):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.get(base_url + url)
        logging_helper(response)
    return response


def delete_request(url, json):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.delete(base_url + url, json=json)
        logging_helper(response)
    return response


def get_cookie(user_name=user_name, password=password):
    url = "https://12go.asia/api/nuxt/en/user/auth"
    with step(f"POST {url}"):
        session = requests.Session()
        jsonAuth = json.dumps({"email": user_name, "password": password}, ensure_ascii=False).encode('utf8')
        response = session.post(url, jsonAuth)
        cookies = response.cookies.get_dict()
        logging_helper(response)
        return cookies, response
