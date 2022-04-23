from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("zero_div", views.zero_div_error, name='zero_div'),
    path("admin/", admin.site.urls),
    path("", include("profiles.urls", namespace="profiles")),
    path("", include("lettings.urls", namespace="lettings")),
]
