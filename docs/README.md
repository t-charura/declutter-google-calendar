# Google Calendar CLI / Declutter Google Calendar


**CLI to batch delete multiple Google Calendar events 📆**

* Delete all events within a specific time period
* Delete past entries of a specific recurring event series 

---

**Documentation:** [Official Website](https://t-charura.github.io/gcal-cli/)

**Source Code:** [Github](https://github.com/t-charura/gcal-cli)

---

## About the Project

<img style="float: right;" src="img/declutter.jpg" width="200">

Did you ever want to declutter your Google Calendar? Or get rid of old and irrelevant calendar events?

You probably realised that neither the Google Calendar app nor the website offer the functionality to batch delete multiple events at once. After deleting more than 100 events from my calendar by hand, I created this CLI program to automate the process. 


### Build with
* <img src="img/python.png" width="20" style="vertical-align:middle"> [Python](https://www.python.org/) 

* <img src="img/google.png" width="20" style="vertical-align:middle"> [Google Api Python Client](https://github.com/googleapis/google-api-python-client)

* <img src="img/typer.png" width="30" style="vertical-align:middle"> [Typer](https://github.com/tiangolo/typer)

---

## Prerequisites

* [Google Cloud Platform Project](https://developers.google.com/workspace/guides/create-project)
* [Create and download credentials](https://developers.google.com/workspace/guides/create-credentials)
    * Credentials for a desktop application

---

## Installation

### Using **Poetry** (recommended)

If you are not already a poetry user, have a look at the [official documentation](https://python-poetry.org/docs/) and install poetry for your operating system.

Next, execute the following commands to clone the project to your local machine via HTTPS or SSH, cd into the project, create a virtual environment and install the package to get access to the ```gcal``` command.

```console
$ git clone https://github.com/t-charura/gcal-cli.git
$ cd gcal-cli
$ poetry shell   # create a virtual environment
$ poetry install   # install the package
```

### Without using **Poetry**
Another way to install the package is to use the `pyproject.toml` directly. Since poetry is
not used, I recommend that you create and activate a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) before executing the following commands.
```console
$ git clone https://github.com/t-charura/gcal-cli.git
$ cd gcal-cli
$ python -m pip install .   # uses the pyproject.toml to install the package
```

### Using **pip**
Coming soon ... 

---

## How to use

Now you should have access to the ```gcal``` command.

Please run
```console
$ gcal --help 
```
to make sure that everything was installed correctly and to read about how to use the CLI in detail. 


### Authentication

Before you can start decluttering your Calendar, you have to generate a token that lets you access your Google Calendar. 
Please run the following command in the directory that stores your credentials ("credentials.json"). 

```console
$ gcal generate-token
```

### Batch delete events
* use description of --help commands to generate quick info here (describe basic and refer to --help command again)

Batch
```console
$ gcal delete batch
```
Recurrence
```console
$ gcal delete recurrence
```


---

## Next Steps

* [ ] Publish on pypi.org
* [ ] Add other methods of authentication

---

## Licence

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

**Email:** tendai.charura@gmail.com

**Github:** [t-charura](https://github.com/t-charura)


---


## My Todos (not part of the readme)

* More descriptive package name -> gcal-cli - it is not a general CLI
    * declutter-gcal ?