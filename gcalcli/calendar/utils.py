import os
import sys
from datetime import datetime

import typer
from google_auth_oauthlib.flow import InstalledAppFlow

from gcalcli.config import settings


def create_token_from_credentials():
    """Create and save Token from credentials to access Google Calendar API."""
    cwd = os.getcwd()
    credentials_file = os.path.join(cwd, settings.CREDENTIALS)

    if os.path.isfile(credentials_file):
        flow = InstalledAppFlow.from_client_secrets_file(credentials_file, settings.SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(settings.TOKEN, "w") as token:
            token.write(creds.to_json())
        print("-" * 30)
        print(f"Token was saved at: {settings.TOKEN}")
    else:
        print(f"There is no '{settings.CREDENTIALS}' at {cwd}")
        print("Make sure that your JSON file is spelled correctly and is located in the above mentioned directory.")


def delete_token():
    """Delete Token if it had been set in the past with 'gcal generate-token'"""
    if os.path.isfile(settings.TOKEN):
        os.remove(settings.TOKEN)
        print("Your Token has been removed! Before you can use this CLI again, please generate a new Token")
    else:
        print(f"File '{settings.TOKEN}' does not exist!")


def verify_and_transform_date(date: str) -> str:
    """Transform a string into a RFC3339 timestamp"""
    try:
        return datetime.strptime(date, "%Y-%m-%d").isoformat() + "Z"
    except ValueError:
        print("Please provide your date in the following format: yyyy-mm-dd")
        sys.exit(1)


def print_selection(instance: str, name: str):
    """Print information with color styling"""
    if instance == "calendar":
        instance_color = typer.colors.BRIGHT_BLUE
        event_color = typer.colors.BLUE
    else:
        instance_color = typer.colors.BRIGHT_GREEN
        event_color = typer.colors.GREEN
    instance_style = typer.style(instance, fg=instance_color)
    name_style = typer.style(name, fg=event_color, bold=True)
    typer.echo(f"Selected {instance_style}: {name_style}")


def print_time_period(first: str, last: str):
    """Print information with color styling"""
    first_style = typer.style(first, fg=typer.colors.BRIGHT_MAGENTA)
    second_style = typer.style(last, fg=typer.colors.BRIGHT_MAGENTA)
    typer.echo(f"Delete all instances from {first_style} - {second_style}")
