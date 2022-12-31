import typer

from decluttergcal.calendar.utils import create_token_from_credentials, delete_token
from decluttergcal.cli.delete import delete_app
from decluttergcal.cli.get import get_app

app = typer.Typer()
app.add_typer(delete_app, name="delete", help="Interact with gcal's delete subcommands.")
app.add_typer(get_app, name="get", help="Interact with gcal's get subcommands.")


@app.command()
def generate_token():
    """
    Create a token to access your Google Calendar.

    The token is generated based on your Google credentials. Run this command in the directory that contains your
    Google access credentials. Make sure that your credentials file is named: "credentials.json".
    """
    create_token_from_credentials()


@app.command()
def remove_token():
    """Delete your token if it exists."""
    delete_token()
