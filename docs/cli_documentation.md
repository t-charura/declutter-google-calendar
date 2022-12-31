# `gcal`


**Commands**:

* `delete`: Interact with gcal's delete subcommands.
* `generate-token`: Create a token to access your Google Calendar.
* `get`: Interact with gcal's get subcommands.
* `remove-token`: Delete your token if it exists.

## `gcal delete`

Interact with gcal's delete subcommands

**Commands**:

* `batch`: Batch delete events within a specific time period.
* `recurrence`: Batch delete instances of a recurring event.

### `gcal delete batch`

Batch delete events within a specific time period.

The specific calendar is selected by fuzzy matching with the corresponding parameter.

**Usage**:

```console
$ gcal delete batch [OPTIONS] CALENDAR_NAME MAX_DATE [MIN_DATE]
```

**Arguments**:

* `CALENDAR_NAME`: String to fuzzy match the calendar name.  [required]
* `MAX_DATE`: Delete all events prior to this date (yyyy-mm-dd).  [required]
* `[MIN_DATE]`: Delete all events up until this date (yyyy-mm-dd).

**Options**:

* `--help`: Show this message and exit.

**Example**:
 
If you want to delete all events from the calendar named "Daily Habits" before the 22nd of September 2022:

```console
$ gcal delete batch habits 2022-09-22
```

The argument calendar_name (habits) will be matched to the calendar if it is a substring of the calendar name.
The argument can also be an exact match. Upper & lower case differences are ignored. Be more specific in your
description of calendar_name if there are similar named calendars.

The argument max_date (upper bound, exclusive) indicates that all events prior to this date will be deleted from the
calendar (if min_date is None).

The min_date parameter is optional. If you want to delete events within a time period you have to set min_date in
addition to max_date

For example - delete all events from the calendar named "Daily Habits" between 2022-09-01 and 2022-09-22.

```console
$  gcal delete batch habits 2022-09-22 2022-09-01
```

Be aware of the order of dates. Since max_date is required it is always specified first.

### `gcal delete recurrence`

Batch delete instances of a recurring event.

The specific calendar and event is selected by fuzzy matching with the corresponding parameters (calendar_name & event name).

**Usage**:

```console
$ gcal delete recurrence [OPTIONS] CALENDAR_NAME EVENT_NAME
```

**Arguments**:

* `CALENDAR_NAME`: String to fuzzy match the calendar name.  [required]
* `EVENT_NAME`: String to fuzzy match the recurring event name.  [required]

**Options**:

* `-d, --date TEXT`: Delete all instances prior to this date (yyyy-mm-dd)
* `--help`: Show this message and exit.

**Exmaple**:

If you want to delete all old recurring instances of the event "Daily exercise for 20 min" from the
calendar named "Daily Habits" before the 22nd of September 2022:

```console
$  gcal delete recurrence habits exercise -d 2022-09-22
```

The argument calendar_name (habits) will be matched to the calendar if it is a substring of the calendar name.
The argument event_name (exercise) will be matched to the event if it is a substring of the event name.
The arguments can also be exact matches. Upper & lower case differences are ignored. Be more specific in your
description of calendar_name and event_name if there are similar named calendars or events.

The date value (-d) is optional. If no date value is set, all instances prior to today will be deleted.

## `gcal generate-token`

Create a token to access your Google Calendar.

The token is generated based on your Google credentials. Run this command in the directory that contains your
Google access credentials. Make sure that your credentials file is named: "credentials.json".

**Usage**:

```console
$ gcal generate-token [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `gcal get`

Interact with gcal's get subcommands. 

**Commands**:

* `calendars`: Show all availabe calendars in your Google account. 
* `events`: Show events from a specific calendar. 

### `gcal get calendars`

Show all availabe calendars in your Google account.

**Usage**:

```console
$ gcal get calendars [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `gcal get events`

Show events from a specific calendar

**Usage**:

```console
$ gcal get events [OPTIONS] CALENDAR_NAME
```

**Arguments**:

* `CALENDAR_NAME`: String to fuzzy match the calendar name  [required]

**Options**:

* `--help`: Show this message and exit.

## `gcal remove-token`

Delete your token if it exists.

**Usage**:

```console
$ gcal remove-token [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
