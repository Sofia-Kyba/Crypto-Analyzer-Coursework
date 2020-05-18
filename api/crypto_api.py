from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import ssl


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '611f38ee-0ec7-4c19-9e6d-81fdbd53e356',
}


def get_information():
    """
    (NoneType) ->
    Get information using api and write into the file.
    """
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


get_information()
