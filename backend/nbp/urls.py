from django.urls import path
from . import views 

urlpatterns = [
    path('measures', views.measures, name='index'),
]