from datetime import datetime

from gcalcli.calendar.service import create_service
from gcalcli.calendar.utils import print_selection, print_time_period


class Events:
    def __init__(self) -> None:
        self.service = create_service()
        self.calendar_id = None
        self.event_id = None

    def _set_calendar_id(self, calendar_name: str):
        calendar_name = calendar_name.lower()
        # get all calendars
        all_calendars = self.service.calendarList().list().execute()
        for calendar in all_calendars.get("items"):
            calendar_summary = calendar.get("summary").lower()
            if calendar_name in calendar_summary:
                print_selection("calendar", calendar.get("summary"))
                self.calendar_id = calendar.get("id")

    def _set_event_id(self, event_name: str, time_max: str = None) -> None:
        event_name = event_name.lower()
        # get all events from specified calendar
        calendar_events = (
            self.service.events().list(calendarId=self.calendar_id, timeMax=time_max, singleEvents=True).execute()
        )
        for event in calendar_events.get("items"):
            event_summary = event.get("summary").lower()
            if event_name in event_summary:
                print_selection("event", event.get("summary"))
                self.event_id = event.get("recurringEventId")
                break

    def delete_recurring_event_instances(self, calendar_name: str, event_name: str, date: str):

        self._set_calendar_id(calendar_name)
        self._set_event_id(event_name, date)

        # get all instances of recurring event
        instances = (
            self.service.events().instances(calendarId=self.calendar_id, eventId=self.event_id, timeMax=date).execute()
        )
        first = instances.get("items")[0].get("start").get("dateTime")[:10]
        last = instances.get("items")[-1].get("start").get("dateTime")[:10]
        print_time_period(first, last)
        # delete instances
        for instance in instances.get("items"):
            instance["status"] = "cancelled"
            self.service.events().update(
                calendarId=self.calendar_id, eventId=instance.get("id"), body=instance
            ).execute()

    def batch_delete_by_date(self, calendar_name: str, max_date: str, min_date: str = None):

        self._set_calendar_id(calendar_name)

        events = (
            self.service.events()
            .list(calendarId=self.calendar_id, singleEvents=True, timeMax=max_date, timeMin=min_date)
            .execute()
        )

        # TODO: put into utils - pretty print - number of events / instances
        print("Number of deleted events:", len(events.get("items")))

        for event in events.get("items"):
            self.service.events().delete(calendarId=self.calendar_id, eventId=event["id"]).execute()

        # delete all events between 2 dates
        # delete all events prior to date
        # if min_date in init
        # need max_date
        # if max_date

        # delete ALL events from all calendars
        # delete all events from calendar x
        # if calendar_id set in init

        # default: ALL events from all calendars prior to current date
        # add mind and max date into init
        pass
