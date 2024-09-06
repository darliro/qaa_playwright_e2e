import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    """
    Sensitive data retrieved from environment variables.
    """

    LOGIN: str = os.getenv("LOGIN", "")
    PASSWORD: str = os.getenv("PASSWORD", "")
