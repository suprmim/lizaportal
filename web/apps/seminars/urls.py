from flaskcbv.url import Url, make_urls
from views import myListView, listView, detailsView, assignView
from views import listCRUDView, updateCRUDView, deleteCRUDView

namespases = make_urls(
    Url('', listView(), name="list"),
    Url('my/', myListView(), name="mylist"),
    Url('<pk>/', detailsView(), name="details"),
    Url('<pk>/assign/', assignView.as_view('seminar_assign', assign=True), name="assign"),
    Url('<pk>/unassign/', assignView.as_view('seminar_unassign', assign=False), name="unassign"),
    Url('crud/', listCRUDView(), name="crud_list"),
    Url('crud/<pk>/', updateCRUDView.as_view('seminars_crud_update'), name="crud_update"),
    Url('crud/add/', updateCRUDView.as_view('seminars_crud_create'), name="crud_create"),
    Url('crud/<pk>/del/', deleteCRUDView.as_view('seminars_crud_delete'), name="crud_delete"),
)


