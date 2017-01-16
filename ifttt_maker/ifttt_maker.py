"""
Simple python interface to ifttt maker
"""
import requests
import json


class Ifttt(object):
    def __init__(self, event_name, secret_key):
        self.secret_key = secret_key
        self.url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event_name, self.secret_key)

    def trigger(self, value1=None, value2=None, value3=None):
        # Dafuq is this
        data = {}
        if value1:
            data["value1"] = value1
        if value2:
            data["value2"] = value1
        if value2:
            data["value3"] = value1
        r = requests.post(self.url, data=json.dumps(data), headers={"Content-Type":"application/json"})
        if r.status_code != 200:
            raise IftttException(r.status_code, r.json())
        return (r.status_code, r.content)


class IftttException(Exception):
    def __init__(self, status_code, content):
        messages = content["errors"]
        self.error_msg = ""
        for message in messages:
            self.error_msg += message["message"]
        self.status_code = status_code

    def __str__(self):
        return repr("HTTP Code: %s Message: %s" % (self.status_code, self.error_msg))
