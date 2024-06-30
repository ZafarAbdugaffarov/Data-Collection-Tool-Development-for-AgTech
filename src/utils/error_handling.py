import logging

def setup_logging():
    """
    Set up basic logging configuration.
    Logs will be written to 'app.log' file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='app.log'
    )

def log_error(error):
    """
    Log an error message.
    :param error: The error to be logged
    """
    logging.error(f'An error occurred: {str(error)}')

def retry(exceptions, tries=3, delay=1, backoff=2):
    """
    Retry decorator with exponential backoff.

    :param exceptions: The exception(s) to catch and retry on
    :param tries: Number of times to try before giving up
    :param delay: Initial delay in seconds
    :param backoff: Multiplier for the delay on each retry
    """
    import time
    from functools import wraps

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    log_error(e)
                    mtries -= 1
                    time.sleep(mdelay)
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

#This utility module provides functions for settinig up logging,
# handling errors, and implementing a retry mechanism for API calls.
# These functions enhance the rebustness and reliability of the data collection process.