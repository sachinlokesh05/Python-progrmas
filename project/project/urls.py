from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .swagger_view import schema_view
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fundoo/', include('fundoo.urls')),
    path('fundoo/',schema_view, name="swagger"),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
