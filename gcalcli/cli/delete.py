import typer

from gcalcli.calendar.delete import Events

delete_app = typer.Typer()


@delete_app.command()
def recurrence():
    """TMP: Delete recurring events"""
    gcal = Events()
    gcal.delete_recurring_event_instances(calendar_name="other", event_name="test")


@delete_app.command()
def placeholder():
    """Delete something"""
    pass
