from datetime import datetime

import typer

from gcalcli.calendar import utils
from gcalcli.calendar.delete import Events

delete_app = typer.Typer()


@delete_app.command()
def recurrence(
    calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name"),
    event_name: str = typer.Argument(..., help="String to fuzzy match the event name"),
    date: str = typer.Option(None, "--date", "-d", help="Delete all instances prior to this date (yyyy-mm-dd)"),
):
    """Delete instances of recurring events"""
    if date:
        date = utils.verify_and_transform_date(date)
    else:
        date = datetime.now().isoformat() + "Z"
    gcal = Events()
    gcal.delete_recurring_event_instances(calendar_name=calendar_name, event_name=event_name, date=date)


@delete_app.command()
def placeholder():
    """Delete something"""
    pass
