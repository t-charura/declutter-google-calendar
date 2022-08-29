import typer

from gcalcli.calendar.service import create_service

get_app = typer.Typer()


@get_app.command()
def calendars():
    """Show all availabe calendars"""
    service = create_service()
    all_calendars = service.calendarList().list().execute()
    print("-" * 30)
    for calendar in all_calendars.get("items"):
        print(calendar.get("summary"))
