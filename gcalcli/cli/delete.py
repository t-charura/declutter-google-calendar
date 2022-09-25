from datetime import datetime
from typing import Optional

import typer

from gcalcli.calendar import utils
from gcalcli.calendar.delete import DeleteEvents

delete_app = typer.Typer()


@delete_app.command()
def recurrence(
    calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name"),
    event_name: str = typer.Argument(..., help="String to fuzzy match the recurring event name"),
    date: str = typer.Option(None, "--date", "-d", help="Delete all instances prior to this date (yyyy-mm-dd)"),
):
    """
    Batch delete instances of a recurring event.

    The specific calendar and event is selected by fuzzy matching the corresponding parameters.

    Exmaple: If you want to delete all old recurring instances of the event "Daily exercise for 15 min" from the
    calendar named "Daily Habits" before the 22nd of September 2022:

        'gcal delete recurrence habits exercise -d 2022-09-22'

    The argument calendar_name (habits) will be matched to the calendar if it is a substring of the calendar name.
    The argument event_name (exercise) will be matched to the event if it is a substring of the event name.
    The arguments can also be exact matches. Upper & lower case differences are ignored. Be more specific in your
    description of calendar_name and event_name if there are similar named calendars or events.

    The date value (-d) is optional. If no date value is set, all instances prior to today will be deleted.
    """
    if date:
        date = utils.verify_and_transform_date(date)
    else:
        date = datetime.now().isoformat() + "Z"
    gcal = DeleteEvents()
    gcal.delete_recurring_event_instances(calendar_name=calendar_name, event_name=event_name, date=date)


@delete_app.command()
def batch(
    calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name"),
    max_date: Optional[str] = typer.Argument(..., help="Delete all events prior to this date (yyyy-mm-dd)"),
    min_date: Optional[str] = typer.Argument(None, help="Delete all events up until this date (yyyy-mm-dd)"),
):
    """
    Batch delete events within a specific time period.

    The specific calendar is selected by fuzzy matching the corresponding parameter.

    Example: If you want to delete all events from the calendar named "Daily Habits" before the 22nd of September 2022:

        'gcal delete batch habits 2022-09-22'

    The argument calendar_name (habits) will be matched to the calendar if it is a substring of the calendar name.
    The argument can also be an exact match. Upper & lower case differences are ignored. Be more specific in your
    description of calendar_name if there are similar named calendars.
    The argument max_date (upper bound, exclusive) indicates that all events prior to this date will be deleted from the
    calendar (if min_date is None).
    The min_date parameter is optional. If you want to delete events within a time period you have to set min_date in
    addition to max_date

    Example: Delete all events from the calendar named "Daily Habits" between 2022-09-01 and 2022-09-22.

        'gcal delete batch habits 2022-09-22 2022-09-01'

    Be aware of the order of dates. Since max_date is required it is always specified first.

    """
    if max_date:
        max_date = utils.verify_and_transform_date(max_date)
    if min_date:
        min_date = utils.verify_and_transform_date(min_date)

    gcal = DeleteEvents()
    gcal.batch_delete_by_date(calendar_name=calendar_name, max_date=max_date, min_date=min_date)
