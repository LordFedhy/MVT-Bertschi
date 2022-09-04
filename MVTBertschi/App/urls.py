from django.urls import path
from App.views import Bono,inicio

urlpatterns = [
    path("Bono/", Bono, name="Bonos"),
    path("", inicio, name="inicio"),
    ]