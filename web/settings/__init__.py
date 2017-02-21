FLASKCONFIG = 'flaskconfig'

APPLICATIONS = (
    'main', 
    'index', 
)

DEFAULT_HEADERS = {
    'server' : 'my WEB Server',
}

try:
    from local import *
except Exception as err:
    print "Error in local settings:", err