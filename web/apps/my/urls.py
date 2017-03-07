from flaskcbv.url import Url, make_urls
from views import cabinetView

namespases = make_urls(
    Url('', cabinetView(), name="cabinet"),
)


