import unittest
from unittest.mock import patch
import requests
from io import StringIO
from main import WebPageInfo


class WebPageInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.com"
        self.web_page = WebPageInfo(self.url)

    @patch.object(requests, 'get')
    def test_fetch_page_info_successful(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.headers = {'Content-Type': 'text/html'}
        mock_response.text = '<html><body>Hello World!</body></html>'

        self.web_page.fetch_page_info()

        self.assertEqual(self.web_page.headers, {'Content-Type': 'text/html'})
        self.assertEqual(self.web_page.page_content, '<html><body>Hello World!</body></html>')

    @patch.object(requests, 'get')
    def test_fetch_page_info_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Request error")

        self.web_page.fetch_page_info()

        self.assertIsNone(self.web_page.headers)
        self.assertIsNone(self.web_page.page_content)

    def test_print_headers_with_available_headers(self):
        self.web_page.headers = {'Content-Type': 'text/html', 'Server': 'Apache'}

        expected_output = "Headers:\nContent-Type: text/html\nServer: Apache\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.web_page.print_headers()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_headers_without_available_headers(self):
        self.web_page.headers = None

        expected_output = "No headers available. Please fetch page info first.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.web_page.print_headers()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_write_headers_to_json_without_available_headers(self):
        self.web_page.headers = None
        filename = 'test_headers.json'

        expected_output = "No headers available. Please fetch page info first.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.web_page.write_headers_to_json(filename)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_write_page_content_to_xml_without_available_page_content(self):
        self.web_page.page_content = None
        filename = 'test_page_content.xml'

        expected_output = "No page content available. Please fetch page info first.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.web_page.write_page_content_to_xml(filename)
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
