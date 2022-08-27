import os
import sys

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

from gcalcli.config import settings


def create_service() -> Resource:
    """Construct a Resource for interacting with the Google Calendar API.

    Returns:
        Resource:   A Resource object with methods for interacting with the API.
    """
    if os.path.exists(settings.TOKEN):
        creds = Credentials.from_authorized_user_file(settings.TOKEN_FILE_NAME, settings.SCOPES)
        if not creds.valid and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(settings.TOKEN, 'w') as token:
                token.write(creds.to_json())
    else:
        print('Token does not exist - please create a token with "gcal generate-token"')
        sys.exit(1)
    
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print('An error occurred: %s' % error)
        sys.exit(1)
    except:
        print('Could not connect to the Google Calendar API. Create a new Token')
        sys.exit(1)
        

