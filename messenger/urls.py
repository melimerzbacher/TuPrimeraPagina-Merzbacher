from django.urls import path
from .views import inbox 

app_name = "messenger"

urlpatterns = [
    path("", inbox, name="inbox"),
]

