from flaskcbv.url import Url, make_urls
from views import authView

namespases = make_urls(
    Url('', authView(), name="static"),
)


