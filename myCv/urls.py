from django.urls import path,include
from . import views

urlpatterns = [
    path('cv/',views.cv,name="cv")
]
