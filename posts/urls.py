from django.urls import path

from .views import *

app_name = 'posts'

urlpatterns = [

    path("", index, name="index"),
    path("detail/<int:id>/", detail, name="detail"),
    path("create/", create_view, name="create"),
    path("edit/<int:id>/", edit_view, name="edit"),
    path("delete/<int:id>/", delete_view, name="delete"),
]
