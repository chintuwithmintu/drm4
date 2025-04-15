import os

API_ID = os.environ.get("API_ID", "29940750")

API_HASH = os.environ.get("API_HASH", "33412ad3b366ca991309d1bcbb472c32")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7704139198:AAGzSUJkbAIBlEPt2acAuN4noGmKlC-Ja9k")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7618270428))

LOG = -1002416903653,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[7618270428]
    for x in (os.environ.get("ADMINS", "7618270428").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
