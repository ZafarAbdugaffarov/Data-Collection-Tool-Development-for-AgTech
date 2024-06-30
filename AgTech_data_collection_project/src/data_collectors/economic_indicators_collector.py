import pandas as pd
from .base_collectors import BaseCollector

class EconomicIndicatorsCollector(BaseCollector):
    """
    Collector for economic indicators data from the World Bank API.
    """

    def collect_data(self):
        """
        Collect economic indicator data (GDP and Real Interest Rate) from the World Bank

        :return: Path to CSV file where data is saved
        """

        #Define base URL with closing quotation mark
        base_url = "http://api.worldbank.org/v2/country/all/indicator/"

        #List of inficators (GDP and Real Interest Rate)
        indicators = ['NY.GDP.MKTP.CD', 'FR.INR.RINR']

        all_data = []
        for indicator in indicators:
            params = {
                "format": "json",
                "date": "2010:2023",
                "per_page": 1000
            }

            #Make the API request for each indicator
            data = self.make_request(f"{base_url}{indicator}", params)
            all_data.extend(data[1])

        #convert the collected data to a DataFrame
        df = pd.DataFrame(all_data)

        #Save teh data to the CSV file
        output_path = 'data/economic_indicators.csv'
        df.to_csv(output_path, index=False)
        self.logger.info(f"Data saved to {output_path}")
        return output_path
    
# This collector gethers economic indicator data from the World Bank API
# If focuses on GDP and Real Interest Rate, which could be relevant for fertilizer demand forecasting

