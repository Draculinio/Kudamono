import requests
import json

class Requests:
    def post(self,endpoint,post_json,encoding='utf-8'):
        return requests.request("POST",endpoint,data=json.dumps(post_json).encode(encoding))
