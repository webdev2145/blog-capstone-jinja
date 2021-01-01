import requests
URL = 'https://api.npoint.io/5abcca6f4e39b4955965'


class Post:

    def __init__(self):
        # URL = 'https://api.npoint.io/5abcca6f4e39b4955965'
        self.responses = requests.get(url=URL)
        self.posts = self.responses.json()
