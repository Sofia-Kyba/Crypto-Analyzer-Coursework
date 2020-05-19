### Project name: Crypto Analyzer

Check it out:
http://sofiakyba.pythonanywhere.com/

### Table of contents


### Description

The main aim of Crypto Analyzer Project is to explore tendency
in crypto currency development and prevalence and make it easy to to get acquainted with crypto currencies, understand how to use them and why we need them.

Due to web app user can:
* explore frequency of crypto currency adding to system;
* compare quantity of crypto currency existing coins and circulating ones;
* find all crypto currencies in needed price range;
* explore and compare rating of all recommended mining companies and wallets;
* explore price change of needed crypto currency for last day or week

All information is represented by graphs, charts and tables.

### Input and Output data

All the data was loaded with two kinds of API:

 * General information about crypto currencies: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
 * Information about companies: 
 https://min-api.cryptocompare.com/data/recommended/all
 
 Besides two researches provide user an opportunity to write data he needs.
 
 All output data is represented by graphs, charts and tables.
 
 ## Program structure and content
 
 #### Main modules
 Program can be run by module main.py. It consists of all functions that extract data, use CryptoInfo ADT object that provides needed calculations and builds  all graphs, charts and tables.
 
 Module crypto_adt.py has realisation of CryptoInfo ADT. It consists of methods that help to contain data and make needed changes and calculations with it.
 
 Module dynamic_array.py consists of realisation of needed data structure - Dynamic Array.
 
 You can find them by links below:
 
 
 #### Example modules
 
 
 
 More information about program structure and process of its realisation you can find on the project's wiki.
 
 

### Installation

To run the program you need to install:

`pip install requests`

`pip install flask`

`pip install pandas`

`pip install plotly`

### Usage examples

### Contributing

### Credit

* Kyba Sofia, Ukrainian Catholic University, 2020

### Licence

