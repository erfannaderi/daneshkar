import requests
import json
from xml.etree import ElementTree as eT


class WebPageInfo:
    def __init__(self, url):
        self.url = url
        self.headers = None
        self.page_content = None

    def fetch_page_info(self):
        """
        Fetches information about a web page given its URL and stores the headers and page content.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for a non-successful response status code
            self.headers = response.headers
            self.page_content = response.text
        except requests.RequestException as e:
            print("An error occurred during the HTTP request:", str(e))

    def print_headers(self):
        """
        Prints the headers of the web page.
        """
        if self.headers:
            print("Headers:")
            for key, value in self.headers.items():
                print(key + ":", value)
        else:
            print("No headers available. Please fetch page info first.")

    def write_headers_to_json(self, filename):
        """
        Writes the headers to a JSON file.

        Args:
            filename (str): The name of the JSON file to write.
        """
        if self.headers:
            try:
                serializable_headers = dict(self.headers)  # Convert to a serializable dictionary
                with open(filename, "w") as json_file:
                    json.dump(serializable_headers, json_file, indent=4)
                print("Headers written to", filename)
            except IOError as e:
                print("An error occurred while writing the headers to a JSON file:", str(e))
        else:
            print("No headers available. Please fetch page info first.")

    def write_page_content_to_xml(self, filename):
        """
        Writes the page content to an XML file.

        Args:
            filename (str): The name of the XML file to write.
        """
        if self.page_content:
            try:
                root = eT.Element("PageContent")
                root.text = self.page_content
                tree = eT.ElementTree(root)
                tree.write(filename)
                print("Page content written to", filename)
            except IOError as e:
                print("An error occurred while writing the page content to an XML file:", str(e))
        else:
            print("No page content available. Please fetch page info first.")


url = input("Enter URL: ")

web_page = WebPageInfo(url)
web_page.fetch_page_info()

web_page.print_headers()

web_page.write_headers_to_json("headers.json")

web_page.write_page_content_to_xml("page_content.xml")

