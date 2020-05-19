""" Module for main program of analysing crypto currencies """
# all needed imports
import string
from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import pandas
from modules.crypto_adt import CryptoInfo
from api import company_api, crypto_api

app = Flask(__name__)

# create an object of CryptoInfo ADT
container = CryptoInfo()

# extract information given with API
allData = crypto_api.get_information()
companyData = company_api.get_information()

# put all the information into crypto_adt
container.put_information(allData['data'])


# render the main page with information
@app.route('/', methods=['GET'])
@app.route('/crypto_info', methods=['POST'])
def main_page():
    """ Render main page """
    return render_template('index_.html')


# render page with pie chart that represents information
# about emergence frequency of all crypto currencies
# during last 20 years
@app.route("/emergence", methods=['POST'])
def emergence():
    """
    Define frequency of adding crypto currencies
    to system and render appropriate page
    with diagram and table.
    """
    years, quantity = container.define_frequency()
    colors = ['#6e2226', '#541619', '#750f14',
              '#9c1319', '#bf1d24', '#e32b33',
              '#d9454c', '#cc585d']
    trace = [go.Pie(labels=years, values=quantity,
                    textfont=dict(size=25),
                    marker=dict(colors=colors))]

    # Here we save our diagram as a string
    # in order to insert it in our HTML file.
    pl = plotly.offline.plot(trace, include_plotlyjs=False,
                             output_type='div')

    # Then we insert this diagram as a <div>
    # container into new HTML file
    # write_to_html(pl, "templates/new_emergence_frequency.html")

    # extract needed information and put it to pandas
    # series to use it in dataFrame
    dates = container._dates
    years = []
    for i in dates:
        years.append(i[1][:4])
    newYears = sorted(years[:200])
    names = []
    for year in newYears:
        for j in dates:
            if year in j[1] and (j[0], j[1]) not in names:
                names.append((j[0], j[1]))
                break
    result = []
    for i in range(len(newYears)):
        series = pandas.Series({'YEAR': newYears[i],
                                'NAME': names[i][0],
                                'DATE': names[i][1]})
        result.append(series)

    # Here we save our information as dataFrame
    df = pandas.DataFrame(result).set_index(['YEAR',
                                             'NAME', "DATE"])
    # Then we receive html coding of our table
    htmlDf = df.to_html(classes="table table-striped")
    return render_template('new_emergence_frequency.html', data=pl)


# render page with an opportunity for user to write
# price and receive list with cryptocurrencies
# that has price approximate to written one
@app.route("/approximate_price", methods=['POST'])
def approx_price():
    """
    Render page with form, where user
    can write needed price
    """
    return render_template('approximate_price.html')


@app.route("/approximate_price_answer", methods=['POST'])
def approx_price_answer():
    """
    Define all crypto currencies with closest
    price to needed one and render html
    page with results.
    """
    # We receive needed price from user
    price = request.form['price']
    if checkInput(price, 'approx_price'):
        # We get list with appropriate crypto currencies
        result = container.approximatePrice(float(price))
        if len(result) != 0:
            allLines = []
            for i in result:
                line = '{} - {}'.format(i[0], str(i[1]))
                allLines.append(line)
            return render_template('approximate_price_answer.html',
                                   allLines=allLines[:20])
        allLines = ['No such crypto currencies']
        return render_template('approximate_price_answer.html',
                               allLines=allLines)
    else:
        return render_template('approximate_price.html')


# render page with comparison between quantity of
# existing coins and circulating ones of all
# crypto currencies.
@app.route("/exist_circulate", methods=['POST'])
def existence_circulation():
    """
    Define quantity of existing coins and
    circulating ones of all crypto currencies.
    Create dataFrame and render html page with it.
    """
    crypto = container.get_array()
    circulation_num = container.get_circulation()
    existence_num = container.get_existence()
    all_ = []
    for j in range(len(circulation_num)):
        # We create pandas series
        series = pandas.Series({'Existence': existence_num[j],
                                'Circulation': circulation_num[j]})
        all_.append(series)

    # Here we save our information as dataFrame
    df = pandas.DataFrame(all_, index=crypto)[:190]

    # Then we receive html coding of our table
    htmlDf = df.to_html(classes="table table-striped")
    return render_template('existence_circulation.html')


# render page with current top of mining companies
@app.route("/mining_companies", methods=['POST'])
def mining_companies():
    """
    Define top of companies and wallets and extract
    needed information with API. Build bar charts
    according to their rating and create dataFrame
    with general info. Render html page with results.
    """
    companies, wallets = \
        container.companies(companyData['Data'])

    # lists with all needed info
    # charts and tables will be created
    # according to them
    companyNames, walletNames = [], []
    companyCountries = []
    companyRates, walletRates = [], []
    companyUsers, walletUsers = [], []
    for i in range(len(companies)):
        companyNames.append(companies[i][0])
        companyCountries.append(companies[i][1])
        companyRates.append(companies[i][2])
        companyUsers.append(companies[i][3])
        walletNames.append(wallets[i][0])
        walletRates.append(wallets[i][1])
        walletUsers.append(wallets[i][2])

    # Here we build bar chart with mining companies
    trace = [go.Bar(x=companyNames, y=companyRates)]
    pl = plotly.offline.plot(trace, include_plotlyjs=False,
                             output_type='div')

    # write_to_html(pl, "templates/mining_companies.html")

    # Create pandas series for companies and wallets
    resultCompany = []
    resultWallet = []
    for i in range(len(companyNames)):
        series1 = pandas.Series({'NAME': companyNames[i],
                                 'RATE': companyRates[i],
                                 'COUNTRY': companyCountries[i],
                                 'USERS': companyUsers[i]})
        series2 = pandas.Series({'NAME': walletNames[i],
                                 'RATE': walletRates[i],
                                 'USERS': walletUsers[i]})
        resultCompany.append(series1)
        resultWallet.append(series2)

    # We save our info about companies as dataFrame
    df = pandas.DataFrame(resultCompany, index=[1, 2, 3, 4])
    # Then we receive html coding of our table
    htmlDf = df.to_html(classes="table table-striped")

    # Here we build second bar chart for wallets
    trace2 = [go.Bar(x=walletNames, y=walletRates)]
    pl2 = plotly.offline.plot(trace2, include_plotlyjs=False,
                              output_type='div')

    # write_to_html(pl, "templates/mining_companies.html")

    # We save our info about wallets as dataFrame
    df2 = pandas.DataFrame(resultWallet, index=[1, 2, 3, 4])
    # Then we receive html coding of our table
    htmlDf2 = df2.to_html(classes="table table-striped")
    return render_template('mining_companies.html', data1=pl, data2=pl2)


# render page that represents changes in price
# of each cryptocurrency
@app.route("/price_change", methods=['POST'])
def price_change():
    """
    Render page with form where user can write
    crypto currencies he wants to receive result of
    """
    return render_template('price_change.html')


@app.route("/price_change_answer", methods=['POST'])
def price_change_answer():
    """
    Define changes in needed crypto currency
    price for last day and for last week.
    Build scatter chart with given result and
    render appropriate html page.
    """
    # receive crypto currency written by user
    name = request.form['crypto']
    if checkInput(name, 'price_change'):
        current, changed1day, changed7days \
            = container.price_change(name)
        price = [current, changed1day, changed7days]
        price3 = current
        price2 = changed1day
        price1 = changed7days
        seasons = ['current', 'day change', 'week change']

        # Here we build scatter chart for wallets
        trace = [go.Scatter(x=seasons, y=price)]
        pl = plotly.offline.plot(trace, include_plotlyjs=False,
                                 output_type='div')
        # write_to_html(pl, "templates/price_change_answer.html")
        return render_template('price_change_answer.html',
                               price1=price1, price2=price2,
                               price3=price3, seasons=seasons,
                               name=name)
    else:
        return render_template('price_change.html')


def checkInput(userInput, kind_):
    """
    Check user's input.
    :param userInput: str
    :return: bool
    """
    if kind_ == 'approx_price':
        for i in userInput:
            if i not in string.digits and i != '.':
                return False
        return True
    elif kind_ == 'price_change':
        for i in userInput:
            if i not in string.ascii_lowercase \
                    and i not in string.ascii_letters:
                return False
        return True
    else:
        return


def write_to_html(div, fileName):
    """
    Read and copy an HTML file into new HTML by
    including a new div container. (This is the
    process of merging two different HTML files in Python)
    """
    html_file = open(fileName, 'r')
    html = ''

    for line in html_file:
        line = line.strip()

        # <!--Place Here--> is a placeholder
        # in HTML file for our <div> to be inserted
        if line == "<!--Place Here-->":
            html += div + '\n'
        else:
            html += line + '\n'

    html_file.close()
    with open(fileName,
              'w') as new_html_file:
        new_html_file.write(html)


if __name__ == '__main__':
    app.run(debug=True, port=7000)
