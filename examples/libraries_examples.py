""" Module for demonstrating examples of libraries usage """

# all imports
import json
from requests import Session
from requests.exceptions import ConnectionError,\
    Timeout, TooManyRedirects
import pandas


URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '995673e7-a164-46dd-9e3c-0305ebf49bb5',
}


# TESTING MODULE JSON AND WRITING DATA INTO THE FILE
# TESTING REQUESTS, MODULE SESSION AND EXCEPTIONS
def write_into_file():
    """
    (NoneType) -> dict
    Get information using api, write into the file and
    print all the information..
    """
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(URL, params=parameters)
        data = json.loads(response.text)
        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# TESTING PANDAS
# CREATING TABLE WITH NEEDED DATA
def testing_pandas():
    """
    (NoneType) -> NoneType
    Create a table with such data: name, symbol
    and price of each cryptocurrency.
    """
    data = write_into_file()
    names = []
    symbols = []
    price = []
    full_dict = {}
    for element in data['data']:
        names.append(element['name'])
        symbols.append(element['symbol'])
        price.append(element['quote']['USD']['price'])
    full_dict['NAME'] = names[:50]
    full_dict['SYMBOL'] = symbols[:50]
    full_dict['PRICE'] = price[:50]
    res = pandas.DataFrame.from_dict(full_dict, orient='columns')
    print(res)


if __name__ == '__main__':
    print('TESTING PANDAS...')
    testing_pandas()
