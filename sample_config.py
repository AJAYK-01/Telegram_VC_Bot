HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    # Chat where the bot will play the music.
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
    # Users which have special control over the bot.
    SUDOERS = list(int(x) for x in environ.get("SUDOERS", "").split())
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    SUDOERS = [1243703097, 13216546]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
