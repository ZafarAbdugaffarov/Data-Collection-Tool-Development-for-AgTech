import requests
import pandas as pd
from .base_collectors import BaseCollector

class IndustrySalesCollector(BaseCollector):
    def collect_data(self):
        base_url = "https://quickstats.nass.usda.gov/api/api_GET/"
        params = {
            "key": self.config.get("nass_api_key"),
            "commodity_desc": "FERTILIZER",
            "year__GE": "2010",
            "format": "JSON"
        }
        
        response = self.make_request(base_url, params)
        
        if response and 'data' in response:
            df = pd.DataFrame(response['data'])
            output_path = 'data/industry_sales.csv'
            df.to_csv(output_path, index=False)
            self.logger.info(f"Data saved to {output_path}")
            return output_path
        else:
            self.logger.error("No data received from the API")
            return None

    def make_request(self, url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()