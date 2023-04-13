from django.urls import path
from . import views

urlpatterns = [
    path("plot", views.plotData, name="PlotData"),
    path("all", views.fetchData, name="FetchAllData")
]