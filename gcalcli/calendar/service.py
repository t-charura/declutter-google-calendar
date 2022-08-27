import os
import sys

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

from gcalcli.config import settings


def create_service() -> Resource:
    """Construct a Resource for interacting with the Google Calendar API.

    Returns:
        Resource:   A Resource object with methods for interacting with the API.
    """
    if os.path.exists(settings.TOKEN):
        creds = Credentials.from_authorized_user_file(settings.TOKEN_FILE_NAME, settings.SCOPES)
    else:
        print('Token does not exist')
        sys.exit(1)
        
    if not creds or not creds.valid:
        # TODO: create constants.py - print some nice CLI warning message
        print('CANT CONNECT -- DO SOMETHING (OTHER CLI COMMAND)')
    
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print('An error occurred: %s' % error)
