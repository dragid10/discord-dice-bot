import os

from dotenv import load_dotenv

load_dotenv()  # Read in Environment variables from .env file

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
