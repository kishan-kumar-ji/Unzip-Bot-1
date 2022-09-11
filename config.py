# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("1821674"))
    API_HASH = os.environ.get("d552cde6b6e8dfa7caa453e8d759c921")
    BOT_TOKEN = os.environ.get("5146196225:AAGhFCDQJgx5PWyFhMrYZPcnIXl29L7Blfw")
    LOGS_CHANNEL = int(os.environ.get("-1001263428248"))
    BOT_OWNER = int(os.environ.get("764606033"))
    MONGODB_URL = os.environ.get("mongodb+srv://arup:Arup@2018#cluster0.4auftk4.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("IRmJgBNNU3wJOgLxaH6bBXm6mcNcf0tg")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6