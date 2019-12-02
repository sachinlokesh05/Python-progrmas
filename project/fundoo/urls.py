from fundoo import views
from django.conf.urls import path, include

app_name = 'fundoo'

urlpatterns = [
    path('register', views.registration_view),
]
