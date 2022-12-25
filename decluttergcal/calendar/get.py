from decluttergcal.calendar import CalendarBase, utils


class GetInfo(CalendarBase):
    def get_calendars(self):
        """Show all availabe calendars."""
        all_calendars = self.service.calendarList().list().execute()
        print("Availabe calendars:")
        for calendar in all_calendars.get("items"):
            print("*", calendar.get("summary"))

    def get_events_from_calendar(self, calendar_name: str):
        """Show events from a specific calendar (max 250 entries).

        Args:
            calendar_name (str): Select a specific calendar
        """
        self._set_calendar_id(calendar_name)
        events = self.service.events().list(calendarId=self.calendar_id).execute()
        for event in events.get("items"):
            summary = event.get("summary")
            recurrence = event.get("recurrence")
            if summary:
                utils.print_event_names(summary, recurrence)
