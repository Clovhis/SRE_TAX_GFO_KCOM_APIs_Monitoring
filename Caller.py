import requests
import json
import logging

def get_token(credentials):
    print('Retrieving token..')
    
    url = "https://login.microsoftonline.com/5b973f99-77df-4beb-b27d-aa0c70b8482c/oauth2/token"

    payload = {'grant_type': 'client_credentials',
    'client_secret': credentials.client_secret,
    'client_id': credentials.client_id,
    'resource': credentials.scope
    }

    headers = {
    'Cookie': 'esctx=PAQABBwEAAADnfolhJpSnRYB1SVj-Hgd88XggGyRX_25ZLkBfC445RMtnBTN3eK4ei0DIrYVUwgK7umJIlXmVOe-dm80V1sXSYpBgRPMEdb4wItGFF92yrcEqomf9ITDNDJD8UBVAWH5FjpTctNiiYO1YiKQD8w-rQp-ReWh2xDGCZmhcdjuX44ttfZAKioyl9hCEFvJclUcgAA; fpc=Am3cdgFaFP5MkPvhUebKIEnZVqtnAQAAAFzAvd0OAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    logging.info('Token retrieved')
    
    json_string = response.text
    data = json.loads(json_string)
    access_token = data['access_token']

    return(access_token)

def call_api(url,token,credentials,method,body):
    logging.info('Calling GFO API')
    try:    
        headers = {
            'x-api-key': credentials.api_key,
            'Authorization': 'Bearer ' + str(token),
            'Content-Type': 'application/json'
        }

        response = requests.request(method, url, headers=headers, data=body)

        response_mesagge = str

        if len(str(response.text)) > 0:
            response_mesagge = "ReponseNotEmpty"
        else:
            response_mesagge = "EmptyResponse"

        return(url,response.status_code, response.reason,response_mesagge) 

    except Exception as e:
        logging.error('Exception raised while calling the API. See details')
        logging.info(str(e))
        return(url,0, "Exception raised while calling the API","Couldn't call the API",str(e))