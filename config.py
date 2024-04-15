# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("","25252648"))
    API_HASH = os.environ.get("","17a1e3c7f59dd46196f0570f9df34955")
    BOT_TOKEN = os.environ.get("","7199477809:AAHP3l7vMe_U2LiwQNc657mzqLo4f5re-f0")
    LOGS_CHANNEL = int(os.environ.get('',"-1002032506013"))
    BOT_OWNER = int(os.environ.get("","6986912824"))
    MONGODB_URL = os.environ.get("","mongodb+srv://alienufowala:kxzen@cluster0.ahif6tl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("","IRmJgBNNU3wJOgLxaH6bBXm6mcNcf0tg")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
