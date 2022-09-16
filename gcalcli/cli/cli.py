import typer

from gcalcli.calendar.utils import create_token_from_credentials, delete_token
from gcalcli.cli.delete import delete_app
from gcalcli.cli.get import get_app

app = typer.Typer()
app.add_typer(delete_app, name="delete")
app.add_typer(get_app, name="get")


@app.command()
def generate_token():
    """
    Create a Token based on your Google credentials to access the Google-Calendar API.

    Run this command in the directory that contains your Google access credentials.
    For more help, have a look at the documentation: www.google.com - link is comming soon
    """
    create_token_from_credentials()


@app.command()
def remove_token():
    """Delete your Token if it exists."""
    delete_token()
