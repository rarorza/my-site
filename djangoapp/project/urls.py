from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from project.language import set_language

urlpatterns = [
    path("", include("portfolio.urls")),
    path("blog/", include("blog.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns = [
    # Internacionalization
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
