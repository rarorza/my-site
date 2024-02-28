from django.urls import path
from portfolio import views, api

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index-portfolio"),
    path("api/index/", api.index, name="api-index"),
]
