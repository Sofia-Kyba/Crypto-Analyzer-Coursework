""" Module for creating adt based on Dynamic Array """

# all imports
from modules.dynamic_arrays import DynamicArray


# adt based on Dynamic Array
class CryptoInfo:
    """ Class for representation adt for needed
     information based on array"""

    def __init__(self):
        """
        Create new CryptoInfo object
        """
        # all needed data
        self._allData = {}
        # all cryptocurrencies
        self._cryptoArray = DynamicArray()
        # all cryptocurrencies with date when
        # they were added to system
        self._dates = DynamicArray()
        # array with years
        self._onlyDates = []
        # dictionaries with companies
        self._companies = {}
        self._wallets = {}

    def put_information(self, crypto_dict):
        """
        Add all the information to allData array.
        Add all cryptocurrencies to cryptoArray.
        Add dates when cryptocurrencies were
        added to dates array.
        Add all dates to onlyDates list.
        :return: NoneType
        """
        self._allData = crypto_dict
        for i in range(len(crypto_dict)):
            self._cryptoArray.append(crypto_dict[i]['name'])
            self._dates.append((
                crypto_dict[i]['name'],
                crypto_dict[i]['date_added'][:10]))
            self._onlyDates.append(crypto_dict[i]['date_added'][:4])

    def define_frequency(self):
        """
        Define frequency of adding
        cryptocurrencies to system.
        :return: list, list
        """
        years = []
        quantity = []
        for year in self._onlyDates:
            if year not in years:
                years.append(year)
                quantity.append(self._onlyDates.count(year))
        return years, quantity

    def approximatePrice(self, price):
        """
        Define cryptocurrencies with price that
        is approximate to needed and return list of them.
        :param price: float
        :return: list
        """
        approxPrice = []
        for name in self._cryptoArray:
            crypto = Cryptocurrency(name, self._allData)
            resultPrice = crypto.get_price()
            if price - 200 < resultPrice < price + 200:
                approxPrice.append((name, resultPrice))
        return approxPrice

    def get_existence(self):
        """
        Define how many coins of needed cryptocurrency
        exist now and return list with numbers
        :return: list
        """
        existence = []
        for name in self._cryptoArray:
            crypto = Cryptocurrency(name, self._allData)
            existence.append(crypto.get_existence_num())
        return existence

    def get_circulation(self):
        """
        Define how many coins of needed cryptocurrency
        are in circulation now and return list with numbers
        :return: list
        """
        circulation = []
        for name in self._cryptoArray:
            crypto = Cryptocurrency(name, self._allData)
            circulation.append(crypto.get_circulation_num())
        return circulation

    def price_change(self, name):
        """
        Define changes in price of needed cryptocurrency
        :param name:
        :return: list, list, list, list
        """
        crypto = Cryptocurrency(name, self._allData)
        currentPrice = crypto.get_price()

    def companies(self, companyData):
        """
        Define top mining companies and wallets
        """
        self._companies = companyData['miningcompanies']
        self._wallets = companyData['wallets']
        companies = DynamicArray()
        wallets = DynamicArray()
        for company in self._companies:
            company_ = Company(self._companies[company]['Name'])
            company_.allData = self._companies
            if company_.isRecommended():
                companies.append(company_)
        for wallet in self._wallets:
            wallet_ = Company(self._wallets[wallet]['Name'])
            wallet_.allData = self._wallets
            if wallet_.isRecommended():
                wallets.append(wallet_)
        return companies, wallets

    def get_array(self):
        """
        Return array with names of all cryptocurrencies.
        :return: DynamicArray
        """
        return self._cryptoArray


class Cryptocurrency:
    """ Class for cryptocurrency representation """
    def __init__(self, name, data):
        """
        Create new cryptocurrency object.
        :param name: str
        """
        self.allData = data  # all data about cryptocurrencies
        self.name = name
        self._price = 0
        self._circulation = 0
        self._existence = 0

    # count number of coins in circulation
    def get_circulation_num(self):
        """
        Define and return number of coins in circulation.
        :return: int
        """
        for i in self.allData:
            if i['name'] == self.name:
                self._circulation = i['circulating_supply']
        return self._circulation

    # count number of existing coins
    def get_existence_num(self):
        """
        Define and return number of coins that exist at the moment.
        :return: int
        """
        for i in self.allData:
            if i['name'] == self.name:
                self._existence = i['total_supply']
        return self._existence

    # get price of needed cryptocurrency
    def get_price(self):
        """
        Define and return price of the cryptocurrency.
        :return: int
        """
        for i in self.allData:
            if i['name'] == self.name:
                self._price = i['quote']['USD']['price']
        return self._price


class Company:
    """ Class for minimg company object representation"""
    def __init__(self, name):
        """
        Create new company object
        :param name: str
        """
        self.allData = {}
        self.name = name
        self._averageRate = 0
        self._country = ''
        self._recommended = False

    def isRecommended(self):
        """
        Define whether company is recommended.
        :return: bool
        """
        for i in self.allData:
            if self.name == self.allData[i]['Name']:
                if self.allData[i]['Recommended']:
                    self._recommended = True
                    return True
                return False

    def set_info(self):
        """
        Set country of the company and its
        average rating.
        :return: NoneType
        """
        for i in self.allData:
            if self.name == self.allData[i]['Name']:
                self._country = self.allData[i]['Country']
                self._averageRate =\
                    self.allData[i]["Rating"]["Avg"]
