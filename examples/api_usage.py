# this module is for testing information given with API
# all imports

import json
from requests import Session
from requests.exceptions import ConnectionError,\
    Timeout, TooManyRedirects


URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'APPI_KEY',
}

# here we get information with API key and write it
# into json file


def check(line):
    """
    (str) -> bool
    Check the input, return True if it is
    correct and False otherwise.
    >>> check('abc')
    False
    >>> check('1')
    True
    """
    if line in ('1', '2'):
        return True
    print('Wrong!')
    return False


def write_into_file():
    """
    (NoneType) -> dict
    Get information using api, write into the file and
    return dictionary with all the information.
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


# here we get names of cryptocurrencies and their price

def get_information(option):
    """
    (str) -> NoneType
    Get and print needed information.
    If option == 1 print all the information
    from json file.
    If option == 2 get and print all names
    of cryptocurrencies and their price.
    """
    data = write_into_file()
    if option == '1':
        print('All the data from json file!\n')
        print(data)
    else:
        for element in data['data']:
            name = element['name']
            price = element['quote']['USD']['price']
            cryptocurrency = '{} - {}'.format(name, str(price))
            print(cryptocurrency)


if __name__ == '__main__':
    print("Let's see the examples of API usage...")
    print('Choose what kind of information do you want to see:')
    print('1 - All the information that is saved in json file.')
    print('2 - Names of all current cryptocurrencies and'
          ' their price.')
    answer = input('Your choice: ')
    if check(answer):
        get_information(answer)
