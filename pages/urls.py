
from django.urls import path
from .views import (
    PageListView, PageDetailView,
    PageCreateView, PageUpdateView, PageDeleteView,
)

app_name = "pages"

urlpatterns = [
    path("", PageListView.as_view(), name="page_list"),
    path("<int:pk>/", PageDetailView.as_view(), name="page_detail"),   # usa pk
    path("crear/", PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/editar/", PageUpdateView.as_view(), name="page_update"),
    path("<int:pk>/borrar/", PageDeleteView.as_view(), name="page_delete"),
]