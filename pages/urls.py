
from django.urls import path
from . import views

urlpatterns = [
    path("", views.PagesListView.as_view(), name="pages_list"),
    path("<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("create/", views.PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/edit/", views.PageUpdateView.as_view(), name="page_update"),
    path("<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
]