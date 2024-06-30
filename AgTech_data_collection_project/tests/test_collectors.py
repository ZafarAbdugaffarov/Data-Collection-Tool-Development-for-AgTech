import unittest
from unittest.mock import patch
from src.data_collectors.industry_sales_collector import IndustrySalesCollector

class TestIndustrySalesCollector(unittest.TestCase):
    def setUp(self):
        self.config = {"nass_api_key": "test_key"}
        self.collector = IndustrySalesCollector(self.config)

    @patch('src.data_collectors.industry_sales_collector.requests.get')
    def test_collect_data(self, mock_get):
        # Mock the API response
        mock_get.return_value.json.return_value = {
            "data": [
                {"year": "2020", "value": "1000"},
                {"year": "2021", "value": "1100"}
            ]
        }

        result = self.collector.collect_data()
        self.assertIsNotNone(result)
        self.assertTrue(result.endswith('industry_sales.csv'))

        # Verify that the API was called with the correct parameters
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['key'], "test_key")

if __name__ == '__main__':
    unittest.main()