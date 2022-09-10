from datetime import datetime
from typing import Optional

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
def batch(
    calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name"),
    max_date: Optional[str] = typer.Argument(..., help="max_date"),
    min_date: Optional[str] = typer.Argument(None, help="min_date"),
):
    if max_date:
        max_date = utils.verify_and_transform_date(max_date)
    if min_date:
        min_date = utils.verify_and_transform_date(min_date)

    gcal = Events()
    gcal.batch_delete_by_date(calendar_name=calendar_name, max_date=max_date, min_date=min_date)
