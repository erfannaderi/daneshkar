# Web Page Information Retrieval

This Python program, `main.py`, allows users to fetch information about a web page given its URL, store the headers and page content, and write the headers to a JSON file and the page content to an XML file. The program also includes a test suite in `test.py` to test the functionality of the `WebPageInfo` class.

## main.py

The `main.py` script contains a class `WebPageInfo` that provides the following methods:

- `fetch_page_info`: Fetches information about a web page given its URL and stores the headers and page content.
- `print_headers`: Prints the headers of the web page.
- `write_headers_to_json`: Writes the headers to a JSON file.
- `write_page_content_to_xml`: Writes the page content to an XML file.

The script takes user input for the URL and utilizes the `requests` library to fetch the page information.

## test.py

The `test.py` script contains a test suite using Python's `unittest` module to test the functionality of the `WebPageInfo` class. It includes test cases for successful and error responses, printing headers, and writing headers and page content to files. The tests utilize the `unittest.mock` module to mock the `requests.get` method.

## requirements.txt

The `requirements.txt` file lists the required Python packages and their versions for running the program. The required packages include:
- certifi==2023.11.17
- charset-normalizer==3.3.2
- idna==3.6
- requests==2.31.0
- urllib3==2.1.0

To run the program, first install the required packages using `pip install -r requirements.txt`, and then execute the `main.py` script.

For testing, execute the `test.py` script to run the test suite.



## Authors

- [@erfannaderi](https://github.com/erfannaderi)

