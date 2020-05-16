from django.urls import path

from . import views

# url(r"^/$", .as_view(), name=""),

urlpatterns = [
    path("",views.index,name="index")
]
