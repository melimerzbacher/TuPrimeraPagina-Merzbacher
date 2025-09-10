from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required   # <- DECORADOR requerido
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignUpForm, ProfileForm
from .models import Profile

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Sesión iniciada.")
        return redirect("home")
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada.")
    return redirect("home")

@login_required
def profile_detail(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile_detail.html", {"profile": profile})

@login_required
def profile_update(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Perfil actualizado.")
        return redirect("profile_detail")
    return render(request, "accounts/profile_form.html", {"form": form})

@login_required
def password_change(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Contraseña cambiada.")
        return redirect("profile_detail")
    return render(request, "accounts/password_change.html", {"form": form})
