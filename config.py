import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7487667184:AAF24EpaQJH7491BbxjKqP2nnWSvm1QV-oQ")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24143260"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f65e566d06fc196655413aaf09c9e6e7")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6106998329"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
