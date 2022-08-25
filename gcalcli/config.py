import os


class Settings:

    SCOPES = ['https://www.googleapis.com/auth/calendar']

    TOKEN_DIR =  os.path.join(os.path.dirname( __file__ ), '..', 'token')
    TOKEN_FILE_NAME = 'token.pkl'
    TOKEN = os.path.join(TOKEN_DIR, TOKEN_FILE_NAME)

    CLIENT_SECRET_JSON = 'client_secret.json'

settings = Settings()
