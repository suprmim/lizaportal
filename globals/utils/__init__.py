import inspect

def comes_from(depth=2):
    try:
        frame = inspect.stack()[depth][0]
    except IndexError:
        return "n/a"

    return "{0}<{1}>:{2}".format(frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name)

