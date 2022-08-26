import pickle
from googleapiclient.discovery import build

from gcalcli.calendar.utils import settings


credentials = pickle.load(open(settings.TOKEN, "rb"))
service = build("calendar", "v3", credentials)

cals = service.calendarList().list().execute()
