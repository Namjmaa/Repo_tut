from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_comment, name="comments"),
    path("new/", views.new_comment, name="new_comment"),
]
