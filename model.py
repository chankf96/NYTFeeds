import requests

class Article:
    def __init__(self):
        self.apiurl = 'https://api.nytimes.com'
        self.apikey = '?api-key=wHxPOgApTT1QagnI5VSoGtwrOzn2K7al'
    
    def getArticles(self):
        url = self.apiurl + '/svc/mostpopular/v2/mostviewed/all-sections/7.json' + self.apikey
        r = requests.get(url)
        data = r.json()
        return data
