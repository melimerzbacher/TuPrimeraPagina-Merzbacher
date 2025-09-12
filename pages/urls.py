
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    PageListView, PageDetailView,
    PageCreateView, PageUpdateView, PageDeleteView,
)

app_name = "pages"

urlpatterns = [
    path("", PageListView.as_view(), name="list"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("<int:pk>/", PageDetailView.as_view(), name="page_detail"),
    path("create/", PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/edit/", PageUpdateView.as_view(), name="page_edit"),
    path("<int:pk>/delete/", PageDeleteView.as_view(), name="page_delete"),
]