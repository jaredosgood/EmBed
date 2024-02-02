import time
import openai

def retry_on_rate_limit_error(func, *args, **kwargs):
    """
    A wrapper function that retries the given function after waiting for 5 minutes
    if a RateLimitError is encountered.
    """
    while True:
        try:
            return func(*args, **kwargs)
        except openai.error.RateLimitError as e:
            print("Rate limit reached. Waiting for 5 minutes before retrying...")
            time.sleep(300)  # Wait for 5 minutes (300 seconds)
        except Exception as e:
            # Handle other exceptions as needed
            print(f"An unexpected error occurred: {e}")
            raise e
