from flaskcbv.url import Url, make_urls
from views import listView
from views import listCRUDView

namespases = make_urls(
    Url('', listView(), name="list"),
    Url('crud/', listCRUDView(), name="crud_list"),
)


