from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("blog/", views.main_page, name="index-blog"),
]
