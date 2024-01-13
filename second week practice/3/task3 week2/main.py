import os
import requests
from bs4 import BeautifulSoup
import json
import argparse
from typing import Dict, List


class WebPageInfo:
    def __init__(self, url: str, timeout: int = 10):
        self.url = url
        self.timeout = timeout
        self.page_info: Dict[str, any] = {}

    def get_page_info(self) -> None:
        try:
            response = requests.get(self.url, timeout=self.timeout)
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

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while accessing the webpage: {e}")

    def print_page_info(self, report: bool = False) -> None:
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

        if report:
            print(f"\n{self.url}: {len(self.page_info.get('Page Links', []))} times")

    def save_to_json(self, filename: str) -> None:
        filename = os.path.splitext(filename)[0] + ".json"
        with open(filename, 'w') as file:
            json.dump(self.page_info, file, indent=4)


def parse_arguments():
    parser = argparse.ArgumentParser(description="WebPageInfo - Data Cleaning Program")
    parser.add_argument("-u", "--url", type=str, help="URL address of the web page")
    parser.add_argument("-t", "--timeout", type=int, help="Timeout value for requests")
    parser.add_argument("-r", "--report", action="store_true", help="Save user inputs to a file and print access count")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if not args.url:
        args.url = input("Enter the URL address of the web page: ")

    if not args.timeout:
        args.timeout = int(input("Enter the timeout value for requests: "))

    if not args.report:
        report_input = input("Do you want to save user inputs to a file and print access count? (Y/N): ").lower()
        if report_input == "y":
            args.report = True

    try:
        # Create an instance of the WebPageInfo class
        page_info: WebPageInfo = WebPageInfo(args.url, args.timeout)

        # Access the URL and print the page information
        page_info.get_page_info()

        # Print the page information
        page_info.print_page_info(report=args.report)

        # Save the page information to a JSON file
        if args.report:
            f_name: str = input("Enter the filename for the JSON file: ")
            page_info.save_to_json(f_name)
            print(f"Page information saved to {f_name}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()