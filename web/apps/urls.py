from flaskcbv.url import Url, include, make_urls

import main.urls
import index.urls
import auth.urls
import my.urls

namespases = make_urls(
    Url('/', include(index.urls.namespases, namespace='index')),
    Url('/main/', include(main.urls.namespases, namespace='main')),
    Url('/auth/', include(auth.urls.namespases, namespace='auth')),
    Url('/my/', include(my.urls.namespases, namespace='my')),
)
