from django.contrib import admin
from django.urls import include, path
from generateletter import views
from django.conf.urls import handler404


urlpatterns = [
    path("", include("generateletter.urls")),
    path("admin/", admin.site.urls),
]

handler404 = 'generateletter.views.error_404_view'