import requests
import json
import pytest

BASE_URL="http://httpbin.org/"
IP_URL= "/ip"
POST_TEST_URL ="/post"
LOCAL_IP="175.153.168.0"
class Test_httpbin():

    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]
    
"""  def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name":"yourname","pwd":"123456"}
        r = requests.post(url,data=post_data)
        print(r.headers)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert post_data['name']== response_data["form"]["name"]
        assert post_data['pwd']== response_data["form"]["pwd"] """
    
