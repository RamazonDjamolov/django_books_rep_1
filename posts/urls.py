from django.urls import path

from .views import *

app_name = 'posts'

urlpatterns = [

    path("", index, name="index"),
    path("detail/<int:id>/", detail, name="detail"),
    path("create/", create_view, name="create"),
]
