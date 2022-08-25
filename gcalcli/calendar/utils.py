import os
import pickle

from gcalcli.config import settings
from google_auth_oauthlib.flow import InstalledAppFlow


def create_token_from_credentials(file_path: str = None) -> None:
    """Create and save Token to access Google Calendar from the client-secret JSON.

    Args:
        file_path (str, optional): file path to your JSON client-secret. If None, defaults to current working directory.
    """
    if not file_path:
        file_path = os.getcwd() 
    
    json_file = os.path.join(file_path, settings.CLIENT_SECRET_JSON)

    if os.path.isfile(json_file):
        flow = InstalledAppFlow.from_client_secrets_file(json_file, scopes=settings.SCOPES)
        token = flow.run_console()
        pickle.dump(token, open(settings.TOKEN, 'wb'))
        print('-' * 30)
        print(f'Token was saved at: {settings.TOKEN}')
    else:
        print(f'There is no "{settings.CLIENT_SECRET_JSON}" at {file_path}')
        print('Please make sure that your JSON file is spelled correctly and is located in the above mentioned directory.')


def remove_token():
    """Delete Token if it had been set in the past with 'gcal set-token'"""
    if os.path.isfile(settings.TOKEN):
        os.remove(settings.TOKEN)
    else:
        print(f'File "{settings.TOKEN}" does not exist!')
