import typer
from gcalcli.calendar.utils import create_token_from_credentials, remove_token

app = typer.Typer()


@app.command()
def set_token(file_path: str = None):
    """
    Create Token to access your Google-Calendar.

    Args:
        file_path (str, optional): file path to your JSON client-secret. If None, defaults to current working directory.
    """
    create_token_from_credentials(file_path=file_path)


@app.command()
def delete_token():
    """Delete Token if it exists"""
    remove_token()

