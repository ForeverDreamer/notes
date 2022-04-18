from datetime import datetime as dt
from datetime import timedelta
import pytz


def local_now():
    return dt.now()


def utc_now():
    return dt.now(tz=pytz.UTC)


def utc2local(t):
    return t.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai'))


def local2utc(t):
    return t.replace(tzinfo=pytz.timezone('Asia/Shanghai')).astimezone(pytz.utc) + timedelta(minutes=6)
