# Web Page Information Extraction

This Python script extracts information from a web page, such as the page title, links, and headings, using
the `requests` and `BeautifulSoup` libraries. The extracted information can be printed to the console or saved to a JSON
file.

## Installation

To run the script, you need to have Python 3.x installed on your machine. Additionally, you need to install the required
libraries by running the following command:

```
pip install -r requirements.txt 
```

## Usage

1. Run the script by executing the following command:

   ````
   python web_page_info.py
   ```

2. You will be prompted to enter the URL of the web page you want to extract information from.

3. The script will fetch the page content, extract the relevant information, and display it in the console.

4. Optionally, you can enter a filename to save the extracted information as a JSON file.

## Examples

Here are a few examples of how you can use this script:

1. Extract information from a web page and print it to the console:

   ````
   Enter the URL of the page: https://tiloid.com/
   ```

   The script will fetch the page content, extract the page title, links, and headings, and print them to the console.

2. Extract information from a web page and save it as a JSON file:

   ````
   Enter the URL of the page: https://tiloid.com/
   Enter the filename for the JSON file: page_info.json
   ```

   The script will fetch the page content, extract the information, and save it as a JSON file with the specified filename.

## Limitations

- The script assumes that the web page content is well-formed HTML.
- The script may not work correctly for web pages that require authentication or have complex JavaScript-based
  interactions.

## Authors

- [@erfannaderi](https://github.com/erfannaderi)

