""" Project level settings """
import os

from dotenv import load_dotenv

load_dotenv()

TWITTER_USER = os.getenv("TWITTER_USER")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_API_CALLBACK_URL = os.getenv("TWITTER_API_CALLBACK_URL")
