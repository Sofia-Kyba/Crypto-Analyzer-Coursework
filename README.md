## Project name: Crypto Analyzer

Check it out:
http://sofiakyba.pythonanywhere.com/

## Table of contents

* [Description](#Description)

* [Input and Output data](#Input-and-Output-Data)

* [Program structure and content](#Program-structure-and-content)

* [Installation](#Installation)

* [Usage examples](#Usage-examples)

* [Contributing](#Contributing)

* [Credit](#Credit)

* [Licence](#Licence)



## Description

The main aim of Crypto Analyzer Project is to explore tendency
in crypto currency development and prevalence and make it easy to to get acquainted with crypto currencies,
understand how to use them and why we need them.

Due to web app user can:
* explore frequency of crypto currency adding to system;
* compare quantity of crypto currency existing coins and circulating ones;
* find all crypto currencies in needed price range;
* explore and compare rating of all recommended mining companies and wallets;
* explore price change of needed crypto currency for last day or week

All information is represented by graphs, charts and tables.

## Input and Output data

All the data was loaded with two kinds of API:

* [General information about crypto currencies](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest)
 
* [Information about companies](https://min-api.cryptocompare.com/data/recommended/all)
 
 Besides two researches provide user an opportunity to write data he needs.
 
 All output data is represented by graphs, charts and tables.
 
 ## Program structure and content
 
 ### Main modules
 Program can be run by module **main.py**. It consists of all functions that extract data, use CryptoInfo ADT object that provides needed calculations and builds  all graphs, charts and tables.
 
 Module **crypto_adt.py** has realisation of CryptoInfo ADT. It consists of methods that help to contain data and make needed changes and calculations with it.
 
 Module **dynamic_array.py** consists of realisation of needed data structure - Dynamic Array.
 
 You can find them by links below:
 
 [main.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/modules/main.py)
 
 [crypto_adt.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/modules/crypto_adt.py)
 
 [dynamic_array.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/modules/dynamic_array.py)
 
 ### Modules for extracting data given with api
 
 [crypto_api.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/api/crypto_api.py)
 
 [company_api.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/api/company_api.py)
 
 
 ### Example modules
 
 [adt_example.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/examples/adt_example.py)
 
 [api_usage.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/examples/api_usage.py)
 
 [libraries_examples.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/examples/libraries_examples.py)
 
 [diagrams](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/tree/master/diagrams)
 
 
 More information about program structure and process of its realisation you can find on the project's wiki:
 
 [wiki](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/wiki)
 

## Installation

Firstly clone this repository for usage:

`git clone https://github.com/Sofia-Kyba/Semester_Homework_Ucu.git`

To run the program you need to install:

`pip install requests`

`pip install flask`

`pip install pandas`

`pip install plotly`

## Usage examples

Main page with information about current top-5 cryptocurrencies and side-bar menu:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/main_page.png)

After following 'Emergence Frequency' you will see page with diagram that shows percentage of adding crypto currencies in certain year:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/emergence1.png)

And table with more detailed information:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/emergence2.png)

After following 'Approximate Price' you will have an opportunity to write price which you want to receive list of crypto currencies with closest price for:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/approximate_price.png)

After writing price and pressing buton you will be given a result:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/approximate_price_answer.png)

After following 'Existence vs Circulation' you will see comparison table of quantity of existing coins of each crypto currency and circulating ones:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/existence_circulation2.png)

After following 'Top mining companies' you will receive bar chart according to companies' rating and table with more detailed information about them: 

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/maining_companies.png)

After following 'Price change' you will have an opportunity to write crypto currency you want to know price change for:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/price_change.png)

After writing crypto currency you will receive line graph with price change during last week as result:

![](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/usage_examples/price_change_answer.png)

## Contributing

## Credit

* Kyba Sofia, Ukrainian Catholic University, 2020

## Licence

