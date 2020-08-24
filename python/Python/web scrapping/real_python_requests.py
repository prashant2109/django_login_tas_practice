import requests
from requests.exceptions import HTTPError
import json

try:
    # res = requests.get('https://api.github.com/in')
    res = requests.get('https://google.com/')
    res.raise_for_status()
except HTTPError as http_err:
    print(http_err)
except Exception as e:
    print(e)

git_resp = requests.get('https://api.github.com/search/repositories', params={'q':'requests+language:python'})
print(dir(git_resp))
print(git_resp.json(encoding='utf-8'))


