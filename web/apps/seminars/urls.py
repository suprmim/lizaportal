from flaskcbv.url import Url, make_urls
from views import listView
from views import listCRUDView, updateCRUDView, deleteCRUDView

namespases = make_urls(
    Url('', listView(), name="list"),
    Url('crud/', listCRUDView(), name="crud_list"),
    Url('crud/<pk>/', updateCRUDView.as_view('seminars_crud_update'), name="crud_update"),
    Url('crud/add/', updateCRUDView.as_view('seminars_crud_create'), name="crud_create"),
    Url('crud/del/', deleteCRUDView.as_view('seminars_crud_delete'), name="crud_delete"),
)


