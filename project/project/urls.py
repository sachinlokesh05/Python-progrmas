from django.contrib import admin
from django.conf.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fundoo/', include('fundoo.urls'))
]
