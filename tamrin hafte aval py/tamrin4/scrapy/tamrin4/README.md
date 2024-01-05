
# Currency Spider

This Scrapy spider extracts flag image links, country names, currency names, currency codes, and currency symbols from a webpage and saves the data to a CSV file.

## Installation



1. Install the required dependencies using pip and the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the spider and obtain the data in a CSV file, follow these step:

1. Run the spider using the following command:
   ```bash
   scrapy crawl currency -o output.csv

   ```

The spider will scrape the data and save it to a file named `countries.csv` in the current directory.

## Notes

- Make sure you have Python and Scrapy installed on your system before running the spider.
  ```bash
  pip install scrapy
   ```
- Adjust the spider's code if the HTML structure of the target website changes to ensure accurate data extraction.

## Authors

- [@erfannaderi](https://github.com/erfannaderi)


![Logo](https://github.com/erfannaderi/daneshkar/blob/main/erfan-high-resolution-logo.png?raw=true)
