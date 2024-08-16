from Caller import call_api, get_calls
from Reader import get_urls

for url in get_urls().values():
    call_api(url)

print(get_calls())