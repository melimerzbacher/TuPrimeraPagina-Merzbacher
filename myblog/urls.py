from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls")),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("messenger/", include(("messenger.urls", "messenger"), namespace="messenger")),
    path("pages/", include(("pages.urls", "pages"), namespace="pages")),
    path("ckeditor/", include("ckeditor_uploader.urls")),  
    path("", include("blog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    