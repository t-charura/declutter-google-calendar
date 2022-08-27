import os


class Settings:

    SCOPES = ['https://www.googleapis.com/auth/calendar']

    PROJECT_ROOT_DIR  =  os.path.join(os.path.dirname( __file__ ), '..')
    TOKEN_FILE_NAME = 'token.json'
    TOKEN = os.path.join(PROJECT_ROOT_DIR , TOKEN_FILE_NAME)

    CREDENTIALS = 'credentials.json'

settings = Settings()
