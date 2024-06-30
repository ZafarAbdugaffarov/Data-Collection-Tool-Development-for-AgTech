import requests
from abc import ABC, abstractmethod
import logging

class BaseCollector(ABC):
    """
    Abstract base class for all data collectors.
    Provides common functionality and enforces a standard interface.
    """

    def __init__(self, config):
        """
        Initialize the collector with configuration data.
        :param config: Dictionary containing configuration parameters
        """

        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def collect_data(self):
        """
        Abstract method that must be immplemented by all subclasses.
        This method should contain the logic for collecting data from a specific sources.
        """
        pass
        
   # def make_request(self, url, params=None):
        """
        Make an HTTP GET request to the specified URL.
        :param url: The URL to request data from
        :param params: Optional quesry parameters
        :return: JSON response from the server
        :raises: Logs and re-raises any RequestException
        """

       # try:
     #       response = requests.get(url, params=params)
       #     response.raise_for_status()
       #     return response.json()
        #except requests.RequestsException as e:
        #    self.logger.error(f"Request failed: {str(e)}")
        #    raise

# This base class provides a common struction for all data collectors.
# ensuring consistent error handling and logging across different data sources.
