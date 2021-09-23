from locust import HttpUser, task, between
from locust.contrib.fasthttp import FastHttpUser

class TestUser(FastHttpUser): 
    
    @task
    def viewPage(self):
        self.client.get('/insamlingar/varldshjalte')
        self.client.get('/webpack-runtime-72a2735cd8a1a24911f7.js')
        self.client.get('/framework-3f3b31f3b6fc5c344dca.js')
        self.client.get('/app-9cd3bdb66ddb863d5142.js')
        self.client.get('/styles-407fe62976dc5310c43e.js')
        self.client.get('/commons-16f36d497b002bdafac4.js')
        self.client.get('/9c31700cf97414fc836e3860377cce64191bc134-9c53b563cbb98335accd.js.js')
        self.client.get('/component---src-templates-page-template-tsx-6c62c930e383b3f3ce6b.js')
        self.client.get('/page-data/insamlingar/varldshjalte/page-data.json')
        self.client.get('/page-data/sq/d/1014302582.json')
        self.client.get('/page-data/sq/d/1203226985.json')
        self.client.get('/page-data/sq/d/1677386854.json')
        self.client.get('/page-data/sq/d/187643644.json')
        self.client.get('/page-data/sq/d/28066254.json')
        self.client.get('/page-data/sq/d/3200608417.json')
        self.client.get('/page-data/sq/d/3296809872.json')
        self.client.get('/page-data/sq/d/538779877.json')
        self.client.get('/page-data/app-data.json')
        self.client.get('/logo.svg')
        self.client.get('/eng-flag.svg')
        self.client.get('/logo-rh-sm.svg')
        self.client.get('/logo-rh-md.svg')
        self.client.get('/icon-chevron.svg')
        self.client.get('/logo-90-konto.png')
        self.client.get('/icon-facebook.svg')
        self.client.get('/icon-instagram.svg')
        self.client.get('/icon-twitter.svg')
        self.client.get('/logo-svt.png')
        self.client.get('/logo-sr.png')
        self.client.get('/logo-ur.png')