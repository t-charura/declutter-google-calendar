# Google Calendar CLI 

TODO: more descriptive package name
* declutterGcal ?

**CLI to batch delete multiple Google Calendar events 📆**

---

**Documentation:** [Official Website](https://t-charura.github.io/gcal-cli/)

**Source Code:** [Github](https://github.com/t-charura/gcal-cli)

---

## About the Project

<img style="float: right;" src="img/declutter.jpg" width="100">

* What does the project do?
* Why did you create it?
* Build with ... (Python, Typer, Google-Api-Python-Client)

## Prerequisites

* [Google Cloud Platform Project](https://developers.google.com/workspace/guides/create-project)
* [Create and download credentials](https://developers.google.com/workspace/guides/create-credentials)
    * Credentials for a desktop application


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

### Using **setup.py**
See word.docx
```console
$ git clone https://github.com/t-charura/gcal-cli.git
$ cd gcal-cli
$ python setup.py install
```

### Using **pip**
Coming soon ... 


## How to use

Please use ```--help```

```console
$ gcal --help 
```

### Configuration / SetUp / Verify credentials 

    * Generate Token from credentials
    * Execute command in directory that has credentials
```console
$ gcal generate-token
```

### Batch delete events
```console
$ gcal delete batch
```


## Next Steps

* Publish on pypi.org


## Licence

* Open source


## Contact

* Email: Gmail.com
