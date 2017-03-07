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
    pass
