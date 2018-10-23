import requests
import json

class k_requests:
    def post(self,endpoint,post_json,encoding='utf-8'):
        return requests.request("POST",endpoint,data=json.dumps(post_json).encode(encoding))
    
    def get(self,endpoint):
        return requests.request("GET",endpoint)
        

    def delete(self,endpoint):
        return requests.request("DELETE",endpoint)
