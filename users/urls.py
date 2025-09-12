from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import profile, ProfileUpdateView
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url=reverse_lazy("profile"),
        ),
        name="password_change",
    ),
]