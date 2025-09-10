from django.urls import path
from .views import SignupView, login_view, logout_view, profile_detail, profile_update, password_change

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_update, name="profile_update"),
    path("profile/password/", password_change, name="password_change"),
]
