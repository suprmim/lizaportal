from flaskcbv.url import Url, make_urls
from views import loginView, logoutView
from views import registerView, validateView, revalidateView

namespases = make_urls(
    Url('login/', loginView(), name="login"),
    Url('logout/', logoutView(), name="logout"),


    ## Register new user:
    Url('register/', registerView(), name="register"),

    ## Validate account by validation code in confirm. letter
    Url('validate/', validateView.as_view('registration_validate'), name="validate"),
    Url('validate/<token>/', validateView.as_view('registration_validate_confirm'), name="validate_confirm"),

    ## ReSend confirmation letter:
    Url('revalidate/', revalidateView(), name="revalidate"),
)


