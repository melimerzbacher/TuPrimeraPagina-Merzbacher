from django.shortcuts import render

from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Page
from .forms import PageForm

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"
    
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Page
from .forms import PageForm

class HomeView(TemplateView):
    template_name = "pages/home.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "object_list"  
    ordering = ["-created_at"]  

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(subtitle__icontains=q) | Q(body__icontains=q))
        return qs

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"

class OwnerOrStaffMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object() if hasattr(self, "get_object") else None
        u = self.request.user
        return u.is_staff or (obj and obj.author_id == u.id)

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("pages:page_list")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, OwnerOrStaffMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("pages:page_list")

class PageDeleteView(LoginRequiredMixin, OwnerOrStaffMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("pages:page_list")