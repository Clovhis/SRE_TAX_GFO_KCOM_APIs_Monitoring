import json

def read_json(path):
    data = str    
    with open(path, 'r') as file:
        data = file.read()
    return data

url_dict = {}

def get_urls():
    for key, value in json.loads(read_json()).items():
        print(f"Key: {key} | Value: {value}")
        url_dict[key] = value
    return url_dict
