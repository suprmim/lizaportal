from flaskcbv.url import Url, make_urls
from views import loginView, logoutView

namespases = make_urls(
    Url('login/', loginView(), name="login"),
    Url('logout/', logoutView(), name="logout"),
)


