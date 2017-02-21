from flaskcbv.url import Url, include, make_urls

import main.urls
import index.urls

namespases = make_urls(
    Url('/', include(index.urls.namespases, namespace='index')),
    Url('/main/', include(main.urls.namespases, namespace='main')),
)
