import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError

from decluttergcal.calendar import utils
from decluttergcal.config import settings


class CalendarBase:
    def __init__(self):
        self.service = self._create_service()
        self.calendar_id = None
        self.event_id = None

    def _create_service(self) -> Resource:
        """Construct a Resource for interacting with the Google Calendar API.

        Returns:
            Resource: A Resource object with methods for interacting with the API.
        """
        if os.path.exists(settings.TOKEN):
            creds = Credentials.from_authorized_user_file(settings.TOKEN_FILE_NAME, settings.SCOPES)
            if not creds.valid and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                with open(settings.TOKEN, "w") as token:
                    token.write(creds.to_json())
        else:
            print('Token does not exist - please create a token with "gcal generate-token"')
            sys.exit(1)

        try:
            service = build("calendar", "v3", credentials=creds)
            return service
        except HttpError as error:
            print("An error occurred: %s" % error)
            sys.exit(1)
        except:
            print("Could not connect to the Google Calendar API. Create a new Token")
            sys.exit(1)

    def _set_calendar_id(self, calendar_name: str):
        """Set calendar id based on user input"""
        calendar_name = calendar_name.lower()
        # get all calendars
        all_calendars = self.service.calendarList().list().execute()
        for calendar in all_calendars.get("items"):
            calendar_summary = calendar.get("summary").lower()
            if calendar_name in calendar_summary:
                utils.print_selection("calendar", calendar.get("summary"))
                self.calendar_id = calendar.get("id")
                break
        else:
            print(f'Could not find a calendar that matches "{calendar_name}"')
            sys.exit(1)

    def _set_event_id(self, event_name: str, time_max: str = None):
        """Set event id based on user input"""
        event_name = event_name.lower()
        # get all events from specified calendar
        calendar_events = (
            self.service.events().list(calendarId=self.calendar_id, timeMax=time_max, singleEvents=True).execute()
        )
        for event in calendar_events.get("items"):
            event_summary = event.get("summary").lower()
            if event_name in event_summary:
                utils.print_selection("event", event.get("summary"))
                self.event_id = event.get("recurringEventId")
                break
        else:
            print(f'Could not find an event that matches "{event_name}"')
            sys.exit(1)
