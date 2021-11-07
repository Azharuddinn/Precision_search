from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("precision/Search",views.data, name = "search")
]
