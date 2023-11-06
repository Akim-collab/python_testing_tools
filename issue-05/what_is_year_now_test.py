import json
import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_valid_YMD_format(self, mock_urlopen):
        datetime_str = '2023-11-06T10:00:00Z'
        mock_response = {'currentDateTime': datetime_str}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')
        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('urllib.request.urlopen')
    def test_valid_DMY_format(self, mock_urlopen):
        datetime_str = '06.11.2023T10:00:00Z'
        mock_response = {'currentDateTime': datetime_str}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')
        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        datetime_str = '2023/11/06T10:00:00Z'
        mock_response = {'currentDateTime': datetime_str}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
