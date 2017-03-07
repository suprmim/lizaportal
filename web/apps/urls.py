from flaskcbv.url import Url, include, make_urls

import index.urls
import auth.urls
import my.urls
import seminars.urls

namespases = make_urls(
    Url('/', include(index.urls.namespases, namespace='index')),
    Url('/auth/', include(auth.urls.namespases, namespace='auth')),
    Url('/my/', include(my.urls.namespases, namespace='my')),
    Url('/seminars/', include(seminars.urls.namespases, namespace='seminars')),
)
