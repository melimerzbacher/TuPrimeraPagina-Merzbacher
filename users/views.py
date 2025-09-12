from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.views.generic import CreateView
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

@login_required
def profile(request):
    # asegura que exista el perfil
    Profile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {"user_obj": request.user})

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        Profile.objects.get_or_create(user=request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {"u_form": u_form, "p_form": p_form})

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"u_form": u_form, "p_form": p_form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        obj, _ = Profile.objects.get_or_create(user=self.request.user)
        return obj
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login") 
