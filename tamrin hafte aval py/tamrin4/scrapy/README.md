# World Countries Information Scraper

This Python program uses Scrapy to scrape the list of world countries' information (name, flag link, etc.) from the
website https://www.currencyremitapp.com/world-currency-symbols and prints each country's information on a separate
line.

## Program Description

The program consists of a Scrapy spider named `CountrySpider` that performs the following tasks:

- Initiates a request to the start URL "https://www.currencyremitapp.com/world-currency-symbols".
- Parses the response to extract information about each country, including the country's name and flag link.
- Prints the name and flag link of each country on a separate line.

## Installation Requirements

To run the program, you will need to have Python and Scrapy installed. Additionally, you will need to install the
required packages listed in the `requirements.txt` file.

### Installation Steps

1. Install Python: If Python is not already installed on your system, download and install it from the official Python
   website: https://www.python.org/downloads/

2. Install Scrapy: You can install Scrapy using pip by running the following command in your terminal or command prompt:

3. Install Required Packages: Install the required packages listed in the `requirements.txt` file by running the
   following command:
   `pip install -r requirements.txt`

## Author

- [@erfannaderi](https://github.com/erfannaderi)
