
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home),
    path('extraction',views.extraction),
    path('help',views.help),
    path('extractionSite',views.extractionSite)
]
