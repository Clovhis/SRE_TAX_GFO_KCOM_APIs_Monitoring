import json
import logging

# ---------------------------------------------------------------------------
# Configuration Reader
# Utility functions for loading API endpoint URLs from a JSON file.
# ---------------------------------------------------------------------------

def read_json(path):
    data = str
    with open(path, 'r') as file:
        data = file.read()
    return data

url_dict = {}

def get_urls(path):
    for key, value in json.loads(read_json(path)).items():
        logging.debug(f"Key: {key} | Value: {value}")
        url_dict[key] = value
    return url_dict
