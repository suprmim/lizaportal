import logging
import datetime
import pytz

from flaskcbv.forms import Form


from misc.tzinfo import myTimeZone

def clean_string_wrapper(func):
    def wrapped(self, value):
        if value is not None:
            value = u"%s" % value
        return func(self, value)
    return wrapped

def clean_int_wrapper(func):
    def wrapped(self, value):
        if value is not None:
            if value == '':
                value = 0
            value = int(value)
        return func(self, value)
    return wrapped

def clean_json_wrapper(func):
    def wrapped(self, value):
        if value is None:
            return None
        if isinstance(value, (str, unicode)):
            value = json.loads(value)
        return func(self, value)
    return wrapped




class updateCRUDForm(Form):

    datetime_format = "%Y/%m/%d %H:%M"
    datetime_tz = 3
    
    @clean_string_wrapper
    def clean_name(self, value):
        return value


    @clean_string_wrapper
    def clean_description(self, value):
        return value


    @clean_string_wrapper
    def clean_body(self, value):
        return value

    @clean_int_wrapper
    def clean_price(self, value):
        return value


    @clean_int_wrapper
    def clean_capacity(self, value):
        return value



    @clean_string_wrapper
    def clean_datebegin(self, value):

        ## Make DateTime Object:
        dt = datetime.datetime.strptime(value, self.datetime_format)

        ## Set timezone:
        dt = dt.replace(tzinfo=myTimeZone(self.datetime_tz))

        ## Convert to UTC:
        dt = dt.astimezone(pytz.utc)

        return dt


