from django.urls import path
from . import views
urlpatterns = [
    path('create-api/',
         views.StudentCreateAPIView.as_view(), name='student-create'),
    path('api/<int:pk>',
         views.SnippetDetail.as_view(), name='student-update')


]
