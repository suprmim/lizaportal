import logging
import datetime
import pytz
from flaskcbv.core import engine

from jinja2.runtime import Undefined

from misc.tzinfo import myTimeZone

def strftime_filter(dt, format='%Y/%m/%d %H:%M', tz=3):
    if dt is None or isinstance(dt, Undefined):
        dt = datetime.datetime.now().replace(tzinfo=pytz.utc)
    return dt.astimezone(myTimeZone(tz)).strftime(format)


engine.app.jinja_env.filters['strftime'] = strftime_filter

