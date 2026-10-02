from django.urls import path
from . import views

app_name = "markenting_app"

urlpatterns = [
    path("extraction/", views.ExtractionView.as_view(), name="extraction"),
]