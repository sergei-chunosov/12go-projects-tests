import logging
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import curlify
from dotenv import load_dotenv
import os
import json

load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')


def post_request(url, json):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, json=json)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response


def get_request(url):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.get(base_url + url)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response


def delete_request(url, json):
    base_url = "https://12go.asia"
    with step(f"POST {url}"):
        response = requests.delete(base_url + url, json=json)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response


def get_cookie(url, user_name=user_name, password=password):
    url = "https://12go.asia/api/nuxt/en/user/auth"
    with step(f"POST {url}"):
        session = requests.Session()
        jsonAuth = json.dumps({"email": user_name, "password": password}, ensure_ascii=False).encode('utf8')
        response = session.post(url, jsonAuth)
        curl = curlify.to_curl(response.request)
        cookies = response.cookies.get_dict()
        logging.info(curlify.to_curl(response.request))
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        return cookies
