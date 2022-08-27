import typer
from gcalcli.calendar.utils import create_token_from_credentials, remove_token

app = typer.Typer()


# TODO: set correct cli arguments based on typer.Argument(help=..)


@app.command()
def generate_token():
    """
    Create Token to access your Google-Calendar API.

    Run this command in the directory that contains your Google access credentials.
    For more help, have a look at the documentation: www.google.com - link is comming soon
    """
    create_token_from_credentials()


@app.command()
def delete_token():
    """Delete Token if it exists"""
    remove_token()


@app.command()
def cli_test():
    from gcalcli.calendar.service import create_service
    service = create_service()
    all_calendars = service.calendarList().list().execute()
    for calendar in all_calendars.get("items"):
        print(calendar.get("summary").lower())

