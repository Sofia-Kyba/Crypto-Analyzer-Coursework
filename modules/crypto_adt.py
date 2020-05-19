""" Module for creating adt based on Dynamic Array """

# all imports
from modules.dynamic_array import DynamicArray


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
            resultPrice = crypto.get_price('current')
            if resultPrice is not None:
                if price - 10 < resultPrice < price + 10:
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
        currentPrice = crypto.get_price('current')
        changedPrice1d = crypto.get_price('1d')
        changedPrice7d = crypto.get_price('7d')
        return currentPrice, changedPrice1d, changedPrice7d

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
                company_.set_info('company')
                companies.append([company_.name,
                                  company_.get_country(),
                                  company_.get_rate(),
                                  company_.get_totalUsers()])
        for wallet in self._wallets:
            wallet_ = Company(self._wallets[wallet]['Name'])
            wallet_.allData = self._wallets
            if wallet_.isRecommended():
                wallet_.set_info('wallet')
                wallets.append([wallet_.name,
                                wallet_.get_rate(),
                                wallet_.get_totalUsers()])
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
    def get_price(self, type_):
        """
        Define and return price of the cryptocurrency.
        :return: int
        """
        for i in self.allData:
            if i['name'] == self.name:
                self._price = i['quote']['USD']['price']
                if type_ == 'current':
                    price = self._price
                else:
                    percentage = 0
                    percentage1 = self._price / 100
                    if type_ == '1d':
                        percentage = i['quote']['USD']["percent_change_24h"]
                    elif type_ == '7d':
                        percentage = i['quote']['USD']["percent_change_7d"]
                    percentageChange = percentage1 * percentage
                    price = self._price + percentageChange
                return price


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
        self._totalUsers = 0

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
            else:
                return

    def set_info(self, type_):
        """
        Set country of the company and its
        average rating.
        :return: NoneType
        """
        for i in self.allData:
            if self.name == self.allData[i]['Name']:
                if type_ == 'company':
                    self._country = self.allData[i]['Country']
                self._totalUsers = \
                    self.allData[i]['Rating']['TotalUsers']
                self._averageRate = \
                    self.allData[i]["Rating"]["Avg"]

    def get_country(self):
        """
        Return country of the company or wallet
        :return: str
        """
        return self._country

    def get_rate(self):
        """
        Return country of the company
        :return:
        """
        return self._averageRate

    def get_totalUsers(self):
        """
        Return quantity of users of the company or wallet
        :return: int
        """
        return self._totalUsers
