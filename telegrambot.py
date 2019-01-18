import requests
import socket

from requests.auth import HTTPDigestAuth


class teleBot:
    def __init__(self, token):
        self.auth = HTTPDigestAuth("raspopovmt", "N7c5LaW")
        self.proxie = "http://181.214.112.2:65234"
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(
            token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params, proxies = self.proxie)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params, proxies = self.proxie)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update
