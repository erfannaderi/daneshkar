import os

import requests
from bs4 import BeautifulSoup
import json
from typing import Dict, List


class WebPageInfo:
    def __init__(self, url: str):
        self.url = url
        self.page_info: Dict[str, any] = {}

    def get_page_info(self) -> None:
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Page Title
            page_title = soup.title.string
            self.page_info['Page Title'] = page_title

            # Page Links
            page_links: List[str] = []
            for link in soup.find_all('a'):
                page_links.append(link.get('href'))
            self.page_info['Page Links'] = page_links

            # Headings
            headings: Dict[str, List[str]] = {}
            for i in range(1, 7):
                heading_tags = [tag.string for tag in soup.find_all(f'h{i}')]
                headings[f'h{i}'] = heading_tags
            self.page_info['Headings'] = headings

    def print_page_info(self) -> None:
        print("Page Title:")
        print(self.page_info.get('Page Title'))

        print("\nPage Links:")
        for link in self.page_info.get('Page Links', []):
            print(link)

        print("\nHeadings:")
        headings = self.page_info.get('Headings', {})
        for heading, tags in headings.items():
            print(f"{heading}:")
            for tag in tags:
                print(tag)

    def save_to_json(self, filename: str) -> None:
        filename = os.path.splitext(filename)[0] + ".json"
        with open(filename, 'w') as file:
            json.dump(self.page_info, file, indent=4)


try:
    # Get the URL from the user
    user_input: str = input("Enter the URL of the page: ")

    # Create an instance of the WebPageInfo class
    page_info: WebPageInfo = WebPageInfo(user_input)

    # Get the page information
    page_info.get_page_info()

    # Print the page information
    page_info.print_page_info()

    # Save the page information to a JSON file
    f_name: str = input("Enter the filename for the JSON file: ")
    page_info.save_to_json(f_name)
    print(f"Page information saved to {f_name}")
except Exception as e:
    print(e)
