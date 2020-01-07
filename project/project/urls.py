from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .swagger_view import schema_view
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('fundoo.urls')),
    path('notes/', include('note.urls')),
    url('fundoo/', schema_view, name="swagger"),
    path(r'oauth/', include('social_django.urls', namespace='social')),  # <--
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
