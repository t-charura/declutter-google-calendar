import typer

from gcalcli.calendar.get import GetInfo

get_app = typer.Typer()


@get_app.command()
def calendars():
    """Show all availabe calendars."""
    gcal = GetInfo()
    gcal.get_calendars()


@get_app.command()
def events(calendar_name: str = typer.Argument(..., help="String to fuzzy match the calendar name")):
    """Show events from a specific calendar"""
    gcal = GetInfo()
    gcal.get_events_from_calendar(calendar_name)
    pass
