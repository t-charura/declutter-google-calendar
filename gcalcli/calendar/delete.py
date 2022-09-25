from gcalcli.calendar import CalendarBase, utils


class DeleteEvents(CalendarBase):
    """Class for batch deleting calendar entries"""

    def delete_recurring_event_instances(self, calendar_name: str, event_name: str, date: str):
        """Batch delete instances of a recurring event.

        Args:
            calendar_name (str): Select a specific calendar
            event_name (str): Select the recurring event
            date (str): Delete all instances prior to the date (yyyy-mm-dd)
        """
        self._set_calendar_id(calendar_name)
        self._set_event_id(event_name, date)
        # get all instances of recurring event
        instances = (
            self.service.events().instances(calendarId=self.calendar_id, eventId=self.event_id, timeMax=date).execute()
        )
        first = instances.get("items")[0].get("start").get("dateTime")[:10]
        last = instances.get("items")[-1].get("start").get("dateTime")[:10]
        utils.print_time_period(first, last)
        # delete instances
        for instance in instances.get("items"):
            instance["status"] = "cancelled"
            self.service.events().update(
                calendarId=self.calendar_id, eventId=instance.get("id"), body=instance
            ).execute()

    def batch_delete_by_date(self, calendar_name: str, max_date: str, min_date: str = None):
        """Batch delete events within a specific time period.

        Args:
            calendar_name (str): Select a specific calendar
            max_date (str): Delete all events prior the date (yyyy-mm-dd)
            min_date (str, optional): Delete all events between max_date (upper bound) and min_date (yyyy-mm-dd). Defaults to None.
        """
        self._set_calendar_id(calendar_name)
        # get all events within the specified time period
        events = (
            self.service.events()
            .list(calendarId=self.calendar_id, singleEvents=True, timeMax=max_date, timeMin=min_date)
            .execute()
        )
        # TODO: put into utils - pretty print - number of events / instances
        print("Number of deleted events:", len(events.get("items")))
        for event in events.get("items"):
            self.service.events().delete(calendarId=self.calendar_id, eventId=event["id"]).execute()
