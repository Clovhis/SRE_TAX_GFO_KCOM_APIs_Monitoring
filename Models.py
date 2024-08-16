import os

class Config:
    scope = str 
    client_id = str 
    client_secret = str
    grant_type = str 
    api_key = str

    def __init__(self, scope, client_id, client_secret, grant_type, api_key):
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.api_key = api_key

class APIs:
    url = str
    response_code = int
    status = str
    error_message = str
    def __init__(self, url, response_code, status, error_message):
        self.url = url
        self.response_code = response_code
        self.status = status
        self.error_message = error_message

class Logger:
    event = str
    date = str
    message = str
    def __init__(self,event,date,message):
        self.event = event
        self.date = date
        self.message = message