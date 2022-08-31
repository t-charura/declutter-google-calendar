import typer

from gcalcli.calendar.delete import Events

delete_app = typer.Typer()


@delete_app.command()
def recurrence(
    calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name"),
    event_name: str = typer.Argument(..., help="String to fuzzy match the event name"),
):
    """Delete instances of recurring events"""
    gcal = Events()
    gcal.delete_recurring_event_instances(calendar_name=calendar_name, event_name=event_name)


@delete_app.command()
def placeholder():
    """Delete something"""
    pass
