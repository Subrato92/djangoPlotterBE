from django.urls import path, include
from . import views

urlpatterns = [
    path("csv", views.uploadCsv, name="UploadCsv")
]