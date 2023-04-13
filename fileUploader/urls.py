from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("csv", csrf_exempt(views.uploadCsv), name="UploadCsv")
]