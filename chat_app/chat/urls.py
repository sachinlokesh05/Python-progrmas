from django.conf.urls import url
from . import views
from django.contrib.auth import logout

urlpatterns = [
    # URL form : "/api/messages/1/2"
    url('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    url('api/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    url('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    url('api/users/', views.user_list, name='user-list'),   # POST for new user and GET for all users list
    url('', views.index, name='index'),
    url('register', views.register_view, name='register'),
    url('chat', views.chat_view, name='chats'),
    url('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),    
    url('logout', logout, {'next_page': 'index'}, name='logout'),]