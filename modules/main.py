""" Module for main program of analysing cryptocurrencies """

# all needed imports
from flask import Flask, render_template
import plotly
import plotly.graph_objects as go
from modules.crypto_adt import CryptoInfo
from api import company_api, crypto_api

app = Flask(__name__)
all_data = crypto_api.get_information()
container = CryptoInfo()

company_data = company_api.get_information()
# put all the information into crypto_adt

container.put_information(all_data['data'])


# render the main page with information
@app.route('/', methods=['GET'])
@app.route('/crypto_info', methods=['POST'])
def main_page():
    return render_template('index.html')


# render page with pie chart that represents information
# about emergence frequency of all cryptocurrencies
# during last 20 years
@app.route("/emergence", methods=['POST'])
def emergence():
    years, quantity = container.define_frequency()
    colors = ['#6e2226', '#541619', '#750f14',
              '#9c1319', '#bf1d24', '#e32b33',
              '#d9454c', '#cc585d']
    trace = [go.Pie(labels=years, values=quantity,
                    textfont=dict(size=25),
                    marker=dict(colors=colors))]

    # Here we save our diagram as a string
    # in order to insert it in our HTML file.
    pl = plotly.offline.plot(trace, include_plotlyjs=False, output_type='div')

    # Then we insert this diagram as a <div> container into new HTML file
    write_to_html(pl, "../templates/new_emergence_frequency.html")

    return render_template('new_emergence_frequency.html')


def write_to_html(div, fileName):
    """
    Read and copy an HTML file into new HTML by including a new div container.
    (This is the process of merging two different HTML files in Python)
    """
    html_file = open(fileName, 'r')
    html = ''

    for line in html_file:
        line = line.strip()

        # <!--Place Here--> is a placeholder in HTML file
        # for our <div> to be inserted
        if line == "<!--Place Here-->":
            html += div + '\n'
        else:
            html += line + '\n'

    html_file.close()
    with open("../templates/new_emergence_frequency.html", 'w') as new_html_file:
        new_html_file.write(html)


# render page with an opportunity for user to write
# price and receive list with cryptocurrencies
# that has price approximate to written one
@app.route("/approximate_price", methods=['POST'])
def approx_price():
    return render_template('approximate_price.html')


# render page with comparison between quantity of
# existing coins and circulating coins of all cryptocurrencies.
# @app.route("/exist_circulate", methods=['POST'])
def existence_circulation():
    crypto = container.get_array()
    circulation_num = container.get_circulation()
    existence_num = container.get_existence()
    return render_template('existence_circulation.html')


# render page with current top of mining companies
@app.route("/mining_companies", methods=['POST'])
def mining_companies():
    companies, wallets = \
        container.companies(company_data['Data'])
    # return render_template('mining_companies.html')


# render page that represents changes in price
# of each cryptocurrency
@app.route("/price_change", methods=['POST'])
def price_change():
    return render_template('price_change.html')


if __name__ == '__main__':
    # mining_companies()
    app.run(debug=True, port=6600)
