from fundoo import views
from django.urls import path
from django.conf.urls import include

# app_name = 'fundoo'

urlpatterns = [
    path('register', views.registration_view),
]
