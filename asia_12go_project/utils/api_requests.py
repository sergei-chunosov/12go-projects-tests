import logging
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import curlify


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
