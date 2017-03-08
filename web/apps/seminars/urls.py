from flaskcbv.url import Url, make_urls
from views import listView, detailsView
from views import listCRUDView, updateCRUDView, deleteCRUDView

namespases = make_urls(
    Url('', listView(), name="list"),
    Url('<pk>/', detailsView(), name="details"),
    Url('crud/', listCRUDView(), name="crud_list"),
    Url('crud/<pk>/', updateCRUDView.as_view('seminars_crud_update'), name="crud_update"),
    Url('crud/add/', updateCRUDView.as_view('seminars_crud_create'), name="crud_create"),
    Url('crud/<pk>/del/', deleteCRUDView.as_view('seminars_crud_delete'), name="crud_delete"),
)


