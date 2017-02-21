from flaskcbv.core import engine
from flask_bootstrap import Bootstrap

application = engine.app
application.secret_key = 'f/1Hfw19KaMUx3eEp9fofX19[9j3Z0'

Bootstrap(application)

