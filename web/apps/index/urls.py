from flaskcbv.url import Url, make_urls
from views import indexView

namespases = make_urls(
    Url('', indexView(), name="index"),
)


