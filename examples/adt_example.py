""" Module for representing example of CryptoInfo ADT """

# all imports
import pandas
from modules.crypto_adt import CryptoInfo, Cryptocurrency, Company
from api import crypto_api, company_api


def main():
    """
    Main function for testing and representing
    an example of usage CryptoInfo ADT.
    :return: NoneType
    """
    all_data = crypto_api.get_information()
    company_data = company_api.get_information()

    container = CryptoInfo()
    # extract data
    container.put_information(all_data['data'])

    # extract array with cryptocurrencies
    print('All cryptocurrencies: ')
    allCrypto = []
    for crypto in container.get_array():
        allCrypto.append(crypto)
    print(allCrypto, '\n')

    # define emergence frequency of
    print('Frequency of adding cryptocurrencies to system: ')
    years, quantity = container.define_frequency()
    full_ = {}
    for i in range(len(years)):
        full_[years[i]] = quantity[i]
    result = pandas.Series(full_)
    print(result, '\n')

    # find cryptocurrency with approximate price
    print('Cryptocurrencies with price approximate to yours: ')
    myPrice = 300.4
    print('Your price: ', str(myPrice))
    approxPrice = container.approximatePrice(myPrice)
    if approxPrice is not None:
        res = {}
        final_ = None
        for i in range(len(approxPrice)):
            res[approxPrice[i][0]] = approxPrice[i][1]
            final_ = pandas.Series(res)
        print('Result: ')
        print(final_)

    # compare existence and circulation of first 20 cryptocurrencies
    existence = container.get_existence()
    circulation = container.get_circulation()
    all_ = []
    for j in range(len(circulation)):
        series = pandas.Series({'Existence': existence[j],
                                'Circulation': circulation[j]})
        all_.append(series)
    df = pandas.DataFrame(all_, index=allCrypto)
    print(df[:20])


if __name__ == '__main__':
    main()



