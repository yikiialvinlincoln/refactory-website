from . import views
from django.urls import path

urlpatterns= [
    path('authentication/',views.loginView, name='authentication'),
]