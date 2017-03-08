from flaskcbv.core import engine

from misc.tzinfo import myTimeZone

def strftime_filter(dt, format='%Y/%m/%d %H:%M', tz=3):
    return dt.astimezone(myTimeZone(tz)).strftime(format)


engine.app.jinja_env.filters['strftime'] = strftime_filter

