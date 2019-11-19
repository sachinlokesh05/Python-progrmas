from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
    path('third/', views.third),
    path('fourth/', views.fourth),
    path('login/', views.login),
    path('login/result/', views.result),
]
