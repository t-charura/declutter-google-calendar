from datetime import datetime

from gcalcli.calendar.service import create_service


class Events:
    def __init__(self) -> None:
        self.service = create_service()
        self.calendar_id = None
        self.event_id = None

    def set_calendar_id(self, calendar_name: str):
        calendar_name = calendar_name.lower()
        # get all calendars
        all_calendars = self.service.calendarList().list().execute()
        for calendar in all_calendars.get("items"):
            calendar_summary = calendar.get("summary").lower()
            if calendar_name in calendar_summary:
                print("Selected calendar:", calendar.get("summary"))
                self.calendar_id = calendar.get("id")

    def set_event_id(self, event_name: str, time_max: str = None) -> None:
        event_name = event_name.lower()
        # get all events from specified calendar
        calendar_events = (
            self.service.events().list(calendarId=self.calendar_id, timeMax=time_max, singleEvents=True).execute()
        )
        for event in calendar_events.get("items"):
            event_summary = event.get("summary").lower()
            if event_name in event_summary:
                print("Selected event:", event.get("summary"))
                self.event_id = event.get("recurringEventId")
                break

    def delete_recurring_event_instances(
        self,
        calendar_name: str,
        event_name: str,
        time_max: str = None,
        verbose: bool = True,
    ):
        if not time_max:
            time_max = datetime.now().isoformat() + "Z"

        self.set_calendar_id(calendar_name)
        self.set_event_id(event_name, time_max)

        # get all instances of recurring event
        instances = (
            self.service.events()
            .instances(calendarId=self.calendar_id, eventId=self.event_id, timeMax=time_max)
            .execute()
        )
        if verbose:
            first = instances.get("items")[0].get("start").get("dateTime")[:10]
            last = instances.get("items")[-1].get("start").get("dateTime")[:10]
            print(f"Delete all instances from {first} - {last}")
        # delete instances
        for instance in instances.get("items"):
            instance["status"] = "cancelled"
            self.service.events().update(
                calendarId=self.calendar_id, eventId=instance.get("id"), body=instance
            ).execute()

    def batch_delete_by_time_period():
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
