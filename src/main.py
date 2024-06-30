import yaml
from data_collectors.industry_sales_collector import IndustrySalesCollector
from data_collectors.economic_indicators_collector import EconomicIndicatorsCollector
from utils.error_handling import setup_logging, log_error, retry
import requests

def load_config():
    print("Loading configuration...")
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

@retry(exceptions=(requests.RequestException,), tries=3, delay=1, backoff=2)
def run_collector(collector):
    return collector.collect_data()

def main():
    print("Starting data collection process...")
    setup_logging()
    config = load_config()
    print("Configuration loaded successfully.")

    collectors = [
        IndustrySalesCollector(config),
        EconomicIndicatorsCollector(config)
    ]

    for collector in collectors:
        try:
            print(f"Running {collector.__class__.__name__}...")
            output_path = run_collector(collector)
            print(f"Data collected and saved to {output_path}")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            log_error(e)

    print("Data collection process completed.")

if __name__ == "__main__":
    main()